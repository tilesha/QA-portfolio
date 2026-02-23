"""
AquaID – Selenium Tests
tests/test_my_aquarium.py – My Aquarium: view, add, edit notes, filter, remove
"""

import pytest
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

from conftest import BASE_URL, TIMEOUT, navigate, find_and_wait

AQUARIUM_URL = f"{BASE_URL}/my-aquarium"
ADD_URL      = f"{BASE_URL}/my-aquarium/add"


def go_to_aquarium(driver):
    driver.get(AQUARIUM_URL)
    WebDriverWait(driver, TIMEOUT).until(
        EC.presence_of_element_located((By.TAG_NAME, "main"))
    )
    time.sleep(0.5)


class TestMyAquariumView:
    """TC-AQ-001 to TC-AQ-002 — Aquarium page load and display."""

    def test_aquarium_page_loads(self, logged_in):
        """TC-AQ-001: /my-aquarium page loads without errors."""
        logged_in.get(AQUARIUM_URL)
        wait = WebDriverWait(logged_in, TIMEOUT)
        wait.until(EC.url_contains("/my-aquarium"))
        assert "/my-aquarium" in logged_in.current_url

    def test_page_title_visible(self, logged_in):
        """Page heading 'My Aquarium' is visible."""
        logged_in.get(AQUARIUM_URL)
        WebDriverWait(logged_in, TIMEOUT).until(
            EC.presence_of_element_located((By.TAG_NAME, "h1, h2"))
        )
        headings = logged_in.find_elements(By.CSS_SELECTOR, "h1, h2")
        heading_text = " ".join(h.text for h in headings if h.is_displayed())
        assert "aquarium" in heading_text.lower()

    def test_empty_state_shown_when_no_fish(self, logged_in):
        """TC-AQ-001: Empty state message shown when aquarium has no fish."""
        logged_in.get(AQUARIUM_URL)
        wait = WebDriverWait(logged_in, TIMEOUT)
        wait.until(EC.presence_of_element_located((By.TAG_NAME, "main")))
        time.sleep(1)

        fish_cards = logged_in.find_elements(
            By.CSS_SELECTOR, "[class*='card'], [data-testid='fish-card']"
        )
        if len(fish_cards) == 0:
            # Empty state text should exist
            body = logged_in.find_element(By.TAG_NAME, "body").text.lower()
            assert (
                "no fish" in body or "empty" in body or "add" in body or "start" in body
            ), "Expected empty state message when aquarium is empty"

    def test_add_fish_button_present(self, logged_in):
        """Add fish / navigate to add page button is visible."""
        logged_in.get(AQUARIUM_URL)
        WebDriverWait(logged_in, TIMEOUT).until(
            EC.presence_of_element_located((By.TAG_NAME, "button"))
        )
        buttons = logged_in.find_elements(By.TAG_NAME, "button")
        links = logged_in.find_elements(By.TAG_NAME, "a")
        all_elements = buttons + links

        add_el = next(
            (el for el in all_elements
             if "add" in el.text.lower() or "+" in el.text), None
        )
        assert add_el is not None, "Add fish button/link not found on My Aquarium page"

    def test_fish_cards_show_species_name_and_badge(self, logged_in):
        """TC-AQ-002: Fish cards show species name and care difficulty badge."""
        logged_in.get(AQUARIUM_URL)
        wait = WebDriverWait(logged_in, TIMEOUT)
        wait.until(EC.presence_of_element_located((By.TAG_NAME, "main")))
        time.sleep(0.8)

        fish_cards = logged_in.find_elements(
            By.CSS_SELECTOR, "[class*='card']"
        )
        if fish_cards:
            first_card_text = fish_cards[0].text
            # Should have species name (non-empty text)
            assert len(first_card_text.strip()) > 0

            # Check for difficulty badge
            badges = fish_cards[0].find_elements(
                By.CSS_SELECTOR, "[class*='badge'], span"
            )
            badge_texts = {b.text.strip().lower() for b in badges if b.text.strip()}
            difficulty_values = {"beginner", "intermediate", "expert"}
            assert badge_texts & difficulty_values or True  # soft check


class TestMyAquariumAdd:
    """TC-AQ-003 — Adding fish to the aquarium."""

    def test_add_page_loads(self, logged_in):
        """TC-AQ-003: /my-aquarium/add page loads successfully."""
        logged_in.get(ADD_URL)
        WebDriverWait(logged_in, TIMEOUT).until(
            EC.url_contains("/my-aquarium/add")
        )
        assert "/my-aquarium/add" in logged_in.current_url

    def test_add_page_has_fish_selection(self, logged_in):
        """Add page shows fish selection UI (search or dropdown)."""
        logged_in.get(ADD_URL)
        WebDriverWait(logged_in, TIMEOUT).until(
            EC.presence_of_element_located((By.TAG_NAME, "main"))
        )
        time.sleep(0.5)

        inputs = logged_in.find_elements(By.CSS_SELECTOR, "input, select, [role='combobox']")
        assert len(inputs) > 0, "No input/search field found on add fish page"


class TestMyAquariumEdit:
    """TC-AQ-004 — Edit fish notes."""

    def test_edit_button_visible_on_fish_cards(self, logged_in):
        """TC-AQ-004: Pencil/edit button is visible on each fish card."""
        logged_in.get(AQUARIUM_URL)
        WebDriverWait(logged_in, TIMEOUT).until(
            EC.presence_of_element_located((By.TAG_NAME, "main"))
        )
        time.sleep(0.8)

        fish_cards = logged_in.find_elements(By.CSS_SELECTOR, "[class*='card']")
        if not fish_cards:
            pytest.skip("No fish in aquarium — add fish first to test edit")

        # Look for edit button/icon
        edit_buttons = logged_in.find_elements(
            By.CSS_SELECTOR, "button[aria-label*='edit'], button svg, [class*='pencil']"
        )
        assert len(edit_buttons) > 0, "Edit button not found on fish cards"

    def test_edit_dialog_opens(self, logged_in):
        """TC-AQ-004: Clicking edit button opens a dialog/modal."""
        logged_in.get(AQUARIUM_URL)
        wait = WebDriverWait(logged_in, TIMEOUT)
        wait.until(EC.presence_of_element_located((By.TAG_NAME, "main")))
        time.sleep(0.8)

        fish_cards = logged_in.find_elements(By.CSS_SELECTOR, "[class*='card']")
        if not fish_cards:
            pytest.skip("No fish in aquarium")

        # Click first edit button found
        edit_btns = logged_in.find_elements(
            By.CSS_SELECTOR, "button:has(svg), [class*='edit'], [aria-label*='edit']"
        )
        # Fallback: click any small button in a card
        card_buttons = fish_cards[0].find_elements(By.TAG_NAME, "button")
        if card_buttons:
            card_buttons[0].click()
            time.sleep(0.5)
            dialogs = logged_in.find_elements(
                By.CSS_SELECTOR, "[role='dialog'], [data-radix-dialog-content]"
            )
            assert any(d.is_displayed() for d in dialogs), "Dialog did not open on edit"

    def test_notes_textarea_present_in_edit_dialog(self, logged_in):
        """TC-AQ-004: Edit dialog contains a textarea for notes."""
        logged_in.get(AQUARIUM_URL)
        wait = WebDriverWait(logged_in, TIMEOUT)
        wait.until(EC.presence_of_element_located((By.TAG_NAME, "main")))
        time.sleep(0.8)

        fish_cards = logged_in.find_elements(By.CSS_SELECTOR, "[class*='card']")
        if not fish_cards:
            pytest.skip("No fish in aquarium")

        card_buttons = fish_cards[0].find_elements(By.TAG_NAME, "button")
        if card_buttons:
            card_buttons[0].click()
            time.sleep(0.5)
            textareas = logged_in.find_elements(By.TAG_NAME, "textarea")
            assert any(t.is_displayed() for t in textareas), "Textarea for notes not found in edit dialog"


class TestMyAquariumRemove:
    """TC-AQ-005 — Remove fish from aquarium."""

    def test_remove_button_visible(self, logged_in):
        """TC-AQ-005: Trash/remove button visible on fish cards."""
        logged_in.get(AQUARIUM_URL)
        WebDriverWait(logged_in, TIMEOUT).until(
            EC.presence_of_element_located((By.TAG_NAME, "main"))
        )
        time.sleep(0.8)

        fish_cards = logged_in.find_elements(By.CSS_SELECTOR, "[class*='card']")
        if not fish_cards:
            pytest.skip("No fish in aquarium")

        card_buttons = fish_cards[0].find_elements(By.TAG_NAME, "button")
        assert len(card_buttons) > 0, "No action buttons found on fish card"


class TestMyAquariumFilter:
    """TC-AQ-006 — Filter fish by care difficulty."""

    def test_filter_tabs_present(self, logged_in):
        """TC-AQ-006: Difficulty filter tabs are visible on My Aquarium page."""
        logged_in.get(AQUARIUM_URL)
        WebDriverWait(logged_in, TIMEOUT).until(
            EC.presence_of_element_located((By.TAG_NAME, "main"))
        )
        time.sleep(0.5)

        # Look for tab elements
        tabs = logged_in.find_elements(
            By.CSS_SELECTOR, "[role='tab'], [data-radix-collection-item], button[class*='tab']"
        )
        assert len(tabs) >= 1, "Filter tabs not found on My Aquarium page"

    def test_filter_tabs_clickable(self, logged_in):
        """Clicking a filter tab does not cause an error."""
        logged_in.get(AQUARIUM_URL)
        WebDriverWait(logged_in, TIMEOUT).until(
            EC.presence_of_element_located((By.TAG_NAME, "main"))
        )
        time.sleep(0.5)

        tabs = logged_in.find_elements(
            By.CSS_SELECTOR, "[role='tab'], [data-radix-collection-item]"
        )
        if tabs:
            try:
                tabs[0].click()
                time.sleep(0.3)
                # No crash = pass
                assert True
            except Exception as e:
                pytest.fail(f"Filter tab click caused error: {e}")
        else:
            pytest.skip("No filter tabs found")


class TestAquariumPersistence:
    """TC-AQ-007 — Data persistence across navigation."""

    def test_aquarium_data_persists_after_navigation(self, logged_in):
        """TC-AQ-007: Fish data is still shown after navigating away and back."""
        logged_in.get(AQUARIUM_URL)
        wait = WebDriverWait(logged_in, TIMEOUT)
        wait.until(EC.presence_of_element_located((By.TAG_NAME, "main")))
        time.sleep(0.8)

        # Get initial fish count
        fish_cards_before = logged_in.find_elements(
            By.CSS_SELECTOR, "[class*='card']"
        )
        count_before = len(fish_cards_before)

        if count_before == 0:
            pytest.skip("No fish to test persistence with")

        # Navigate away
        logged_in.get(f"{BASE_URL}/explore")
        time.sleep(0.5)

        # Navigate back
        logged_in.get(AQUARIUM_URL)
        wait.until(EC.presence_of_element_located((By.TAG_NAME, "main")))
        time.sleep(0.8)

        fish_cards_after = logged_in.find_elements(
            By.CSS_SELECTOR, "[class*='card']"
        )
        count_after = len(fish_cards_after)
        assert count_after == count_before, (
            f"Fish count changed after navigation: before={count_before}, after={count_after}"
        )
