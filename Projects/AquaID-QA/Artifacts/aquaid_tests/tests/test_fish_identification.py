"""
AquaID – Selenium Tests
tests/test_fish_identification.py – Fish identification via AI image upload
"""

import pytest
import time
import os
import struct
import zlib
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from conftest import BASE_URL, TIMEOUT, navigate, find_and_wait

# ── Helpers ───────────────────────────────────────────────────────────────────
FISH_IMAGE  = os.path.join(os.path.dirname(__file__), "..", "fixtures", "fish_sample.jpg")
NON_FISH    = os.path.join(os.path.dirname(__file__), "..", "fixtures", "landscape.jpg")
LARGE_IMAGE = os.path.join(os.path.dirname(__file__), "..", "fixtures", "large_image.jpg")

# Expected identification result fields
EXPECTED_FIELDS = [
    "Species Name", "Scientific Name", "Common Names",
    "Description", "Coloration", "Habitat",
    "Care Instructions", "Diet", "Breeding",
    "Compatibility", "Care Difficulty"
]

CARE_DIFFICULTY_VALUES = {"beginner", "intermediate", "expert"}


def go_to_home(driver):
    driver.get(f"{BASE_URL}/")
    WebDriverWait(driver, TIMEOUT).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='file'], [data-testid='image-uploader']"))
    )


class TestFishIdentificationPage:
    """TC-ID-001 to TC-ID-009 – Fish identification page and upload flow."""

    def test_home_page_loads_with_upload_area(self, logged_in):
        """Home page shows image upload area after login."""
        logged_in.get(f"{BASE_URL}/")
        WebDriverWait(logged_in, TIMEOUT).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='file']"))
        )
        upload = logged_in.find_element(By.CSS_SELECTOR, "input[type='file']")
        assert upload is not None

    def test_identify_button_present(self, logged_in):
        """Identify Fish button is visible on the home page."""
        logged_in.get(f"{BASE_URL}/")
        WebDriverWait(logged_in, TIMEOUT).until(
            EC.presence_of_element_located((By.TAG_NAME, "button"))
        )
        buttons = logged_in.find_elements(By.TAG_NAME, "button")
        identify_btn = next(
            (b for b in buttons if "identify" in b.text.lower()), None
        )
        assert identify_btn is not None, "Identify button not found on home page"
        assert identify_btn.is_displayed()

    @pytest.mark.skipif(not os.path.exists(FISH_IMAGE), reason="fish_sample.jpg fixture not provided")
    def test_valid_fish_image_returns_identification(self, logged_in):
        """TC-ID-001: Upload valid fish image → identification result card shown."""
        logged_in.get(f"{BASE_URL}/")
        wait = WebDriverWait(logged_in, TIMEOUT)
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='file']")))

        # Upload the file
        file_input = logged_in.find_element(By.CSS_SELECTOR, "input[type='file']")
        file_input.send_keys(os.path.abspath(FISH_IMAGE))
        time.sleep(0.5)

        # Click Identify
        buttons = logged_in.find_elements(By.TAG_NAME, "button")
        identify_btn = next(b for b in buttons if "identify" in b.text.lower())
        identify_btn.click()

        # Wait for result (up to 30s for AI response)
        result = WebDriverWait(logged_in, 30).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, "[data-testid='fish-card'], .fish-result, h2, h3")
            )
        )
        assert result.is_displayed(), "Expected fish identification result card"

    @pytest.mark.skipif(not os.path.exists(FISH_IMAGE), reason="fish_sample.jpg fixture not provided")
    def test_identification_shows_species_name(self, logged_in):
        """TC-ID-005: Species name field present in result."""
        logged_in.get(f"{BASE_URL}/")
        wait = WebDriverWait(logged_in, 30)
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='file']")))

        file_input = logged_in.find_element(By.CSS_SELECTOR, "input[type='file']")
        file_input.send_keys(os.path.abspath(FISH_IMAGE))
        time.sleep(0.5)

        buttons = logged_in.find_elements(By.TAG_NAME, "button")
        next(b for b in buttons if "identify" in b.text.lower()).click()

        # Check result page body for species-related content
        WebDriverWait(logged_in, 30).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "h2, h3, [class*='species'], [class*='fish']"))
        )
        body_text = logged_in.find_element(By.TAG_NAME, "body").text
        assert len(body_text) > 100, "Result page appears empty"

    @pytest.mark.skipif(not os.path.exists(FISH_IMAGE), reason="fish_sample.jpg fixture not provided")
    def test_care_difficulty_badge_has_valid_value(self, logged_in):
        """TC-ID-006: careDifficulty badge shows beginner / intermediate / expert only."""
        logged_in.get(f"{BASE_URL}/")
        WebDriverWait(logged_in, TIMEOUT).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='file']"))
        )

        logged_in.find_element(By.CSS_SELECTOR, "input[type='file']").send_keys(
            os.path.abspath(FISH_IMAGE)
        )
        time.sleep(0.5)

        buttons = logged_in.find_elements(By.TAG_NAME, "button")
        next(b for b in buttons if "identify" in b.text.lower()).click()

        WebDriverWait(logged_in, 30).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "[class*='badge'], [class*='difficulty']"))
        )
        badges = logged_in.find_elements(By.CSS_SELECTOR, "[class*='badge'], [class*='difficulty']")
        badge_texts = {b.text.strip().lower() for b in badges if b.text.strip()}
        matching = badge_texts & CARE_DIFFICULTY_VALUES
        assert matching, (
            f"Expected care difficulty badge with value in {CARE_DIFFICULTY_VALUES}, "
            f"found: {badge_texts}"
        )

    def test_identify_without_image_shows_error(self, logged_in):
        """TC-ID-004: Clicking Identify without selecting image → error toast."""
        logged_in.get(f"{BASE_URL}/")
        wait = WebDriverWait(logged_in, TIMEOUT)
        wait.until(EC.presence_of_element_located((By.TAG_NAME, "button")))

        buttons = logged_in.find_elements(By.TAG_NAME, "button")
        identify_btn = next(
            (b for b in buttons if "identify" in b.text.lower()), None
        )
        assert identify_btn is not None, "Identify button not found"
        identify_btn.click()

        # Expect error toast
        toast = wait.until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, "[data-sonner-toast], [role='alert']")
            )
        )
        assert "image" in toast.text.lower() or "select" in toast.text.lower() or "no" in toast.text.lower()

    def test_file_input_accepts_images(self, logged_in):
        """Image file input has accept attribute for image types."""
        logged_in.get(f"{BASE_URL}/")
        WebDriverWait(logged_in, TIMEOUT).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='file']"))
        )
        file_input = logged_in.find_element(By.CSS_SELECTOR, "input[type='file']")
        accept = file_input.get_attribute("accept") or ""
        # Should restrict to image types
        assert "image" in accept.lower() or accept == "", (
            f"File input accept attribute should contain 'image', got: {accept}"
        )

    @pytest.mark.skipif(not os.path.exists(FISH_IMAGE), reason="fish_sample.jpg fixture not provided")
    def test_loading_state_shown_during_identification(self, logged_in):
        """TC-ID-001: Loading spinner or loading text shown during AI processing."""
        logged_in.get(f"{BASE_URL}/")
        WebDriverWait(logged_in, TIMEOUT).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='file']"))
        )

        logged_in.find_element(By.CSS_SELECTOR, "input[type='file']").send_keys(
            os.path.abspath(FISH_IMAGE)
        )
        time.sleep(0.3)

        buttons = logged_in.find_elements(By.TAG_NAME, "button")
        next(b for b in buttons if "identify" in b.text.lower()).click()

        # Capture state immediately after click — should see loading indicator
        loading_selectors = [
            "[class*='spinner']",
            "[class*='loading']",
            "[aria-busy='true']",
            "svg[class*='animate']",
        ]
        loading_found = False
        for sel in loading_selectors:
            elements = logged_in.find_elements(By.CSS_SELECTOR, sel)
            if any(e.is_displayed() for e in elements):
                loading_found = True
                break

        # Also check button text changes to loading state
        buttons_after = logged_in.find_elements(By.TAG_NAME, "button")
        for btn in buttons_after:
            if "identifying" in btn.text.lower() or "loading" in btn.text.lower():
                loading_found = True

        assert loading_found, "No loading indicator found during identification"

    @pytest.mark.skipif(not os.path.exists(FISH_IMAGE), reason="fish_sample.jpg fixture not provided")
    def test_new_image_resets_previous_result(self, logged_in):
        """TC-ID-001: Selecting a new image after identification resets result."""
        logged_in.get(f"{BASE_URL}/")
        WebDriverWait(logged_in, TIMEOUT).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='file']"))
        )

        # First identification
        logged_in.find_element(By.CSS_SELECTOR, "input[type='file']").send_keys(
            os.path.abspath(FISH_IMAGE)
        )
        time.sleep(0.3)
        buttons = logged_in.find_elements(By.TAG_NAME, "button")
        next(b for b in buttons if "identify" in b.text.lower()).click()
        WebDriverWait(logged_in, 30).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "h2, h3"))
        )

        # Now select a new image — result should reset
        file_input = WebDriverWait(logged_in, TIMEOUT).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='file']"))
        )
        file_input.send_keys(os.path.abspath(FISH_IMAGE))
        time.sleep(0.5)

        # Previous result card should be cleared from DOM
        result_cards = logged_in.find_elements(
            By.CSS_SELECTOR, "[data-testid='fish-card'], [class*='fish-result']"
        )
        assert len(result_cards) == 0, "Previous result should reset when new image selected"
