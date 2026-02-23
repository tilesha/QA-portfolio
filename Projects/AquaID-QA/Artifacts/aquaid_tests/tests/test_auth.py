"""
AquaID – Selenium Tests
tests/test_auth.py – Authentication: Login, Signup, Forgot Password, Protected Routes
"""

import pytest
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

from conftest import (
    BASE_URL, TEST_EMAIL, TEST_PASS, TEST_EMAIL2, TEST_PASS2,
    TIMEOUT, navigate, find_and_wait, click_and_wait
)


class TestLogin:
    """TC-AUTH-001 to TC-AUTH-007 — Login page behaviour."""

    def test_login_page_loads(self, fresh_driver):
        """Login page renders with email, password fields and submit button."""
        fresh_driver.get(f"{BASE_URL}/login")
        assert find_and_wait(fresh_driver, By.NAME, "email")
        assert find_and_wait(fresh_driver, By.NAME, "password")
        btn = fresh_driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        assert btn.is_displayed()
        assert "Sign in" in btn.text

    def test_valid_login_redirects_to_home(self, fresh_driver):
        """TC-AUTH-001: Valid credentials → redirect to home page."""
        fresh_driver.get(f"{BASE_URL}/login")
        wait = WebDriverWait(fresh_driver, TIMEOUT)
        wait.until(EC.presence_of_element_located((By.NAME, "email")))

        fresh_driver.find_element(By.NAME, "email").send_keys(TEST_EMAIL)
        fresh_driver.find_element(By.NAME, "password").send_keys(TEST_PASS)
        fresh_driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

        wait.until(EC.url_to_be(f"{BASE_URL}/"))
        assert fresh_driver.current_url.rstrip("/") == BASE_URL.rstrip("/")

    def test_login_shows_success_toast(self, fresh_driver):
        """TC-AUTH-001: Toast message 'Login successful' appears after valid login."""
        fresh_driver.get(f"{BASE_URL}/login")
        wait = WebDriverWait(fresh_driver, TIMEOUT)
        wait.until(EC.presence_of_element_located((By.NAME, "email")))

        fresh_driver.find_element(By.NAME, "email").send_keys(TEST_EMAIL)
        fresh_driver.find_element(By.NAME, "password").send_keys(TEST_PASS)
        fresh_driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

        toast = wait.until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, "[data-sonner-toast], [role='status']")
            )
        )
        assert "successful" in toast.text.lower() or "logged in" in toast.text.lower()

    def test_invalid_password_shows_error(self, fresh_driver):
        """TC-AUTH-002: Wrong password → error toast, stays on login page."""
        fresh_driver.get(f"{BASE_URL}/login")
        wait = WebDriverWait(fresh_driver, TIMEOUT)
        wait.until(EC.presence_of_element_located((By.NAME, "email")))

        fresh_driver.find_element(By.NAME, "email").send_keys(TEST_EMAIL)
        fresh_driver.find_element(By.NAME, "password").send_keys("WrongPassword999!")
        fresh_driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

        wait.until(EC.url_contains("/login"))
        # Error toast or inline message
        toast = wait.until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, "[data-sonner-toast], [role='alert']")
            )
        )
        assert "invalid" in toast.text.lower() or "failed" in toast.text.lower()

    def test_unregistered_email_shows_error(self, fresh_driver):
        """TC-AUTH-003: Unregistered email → error, stays on login."""
        fresh_driver.get(f"{BASE_URL}/login")
        wait = WebDriverWait(fresh_driver, TIMEOUT)
        wait.until(EC.presence_of_element_located((By.NAME, "email")))

        fresh_driver.find_element(By.NAME, "email").send_keys("notregistered@example.com")
        fresh_driver.find_element(By.NAME, "password").send_keys("SomePass123!")
        fresh_driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

        wait.until(EC.url_contains("/login"))
        error = wait.until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, "[data-sonner-toast], [role='alert']")
            )
        )
        assert error.is_displayed()

    def test_empty_fields_validation(self, fresh_driver):
        """TC-AUTH-004: Submitting empty form → inline validation errors appear."""
        fresh_driver.get(f"{BASE_URL}/login")
        wait = WebDriverWait(fresh_driver, TIMEOUT)
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "button[type='submit']")))

        fresh_driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        time.sleep(0.5)

        # Expect at least one validation message visible
        errors = fresh_driver.find_elements(By.CSS_SELECTOR, "p[id$='-message'], [role='alert'], .text-red-500")
        assert any(e.is_displayed() for e in errors), "Expected validation error(s) to be visible"

    def test_invalid_email_format_validation(self, fresh_driver):
        """TC-AUTH-005: Invalid email format → inline validation error."""
        fresh_driver.get(f"{BASE_URL}/login")
        wait = WebDriverWait(fresh_driver, TIMEOUT)
        wait.until(EC.presence_of_element_located((By.NAME, "email")))

        fresh_driver.find_element(By.NAME, "email").send_keys("notanemail")
        fresh_driver.find_element(By.NAME, "password").send_keys("password123")
        fresh_driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        time.sleep(0.5)

        errors = fresh_driver.find_elements(By.CSS_SELECTOR, "p[id$='-message'], [role='alert']")
        messages = " ".join(e.text for e in errors if e.is_displayed())
        assert "valid email" in messages.lower() or "email" in messages.lower()

    def test_password_field_is_masked(self, fresh_driver):
        """TC-AUTH-006: Password input type is 'password' (characters masked)."""
        fresh_driver.get(f"{BASE_URL}/login")
        find_and_wait(fresh_driver, By.NAME, "password")
        pwd_field = fresh_driver.find_element(By.NAME, "password")
        assert pwd_field.get_attribute("type") == "password"

    def test_google_sso_button_present(self, fresh_driver):
        """TC-AUTH-007: Google SSO button is visible on login page."""
        fresh_driver.get(f"{BASE_URL}/login")
        find_and_wait(fresh_driver, By.CSS_SELECTOR, "button")
        buttons = fresh_driver.find_elements(By.TAG_NAME, "button")
        google_btn = next(
            (b for b in buttons if "google" in b.text.lower()), None
        )
        assert google_btn is not None, "Google sign-in button not found"
        assert google_btn.is_displayed()

    def test_forgot_password_link_visible(self, fresh_driver):
        """Forgot password link exists and navigates correctly."""
        fresh_driver.get(f"{BASE_URL}/login")
        find_and_wait(fresh_driver, By.PARTIAL_LINK_TEXT, "Forgot")
        link = fresh_driver.find_element(By.PARTIAL_LINK_TEXT, "Forgot")
        link.click()
        WebDriverWait(fresh_driver, TIMEOUT).until(EC.url_contains("/forgot-password"))
        assert "/forgot-password" in fresh_driver.current_url

    def test_signup_link_navigates(self, fresh_driver):
        """'Sign up' link on login page navigates to /signup."""
        fresh_driver.get(f"{BASE_URL}/login")
        find_and_wait(fresh_driver, By.PARTIAL_LINK_TEXT, "Sign up")
        fresh_driver.find_element(By.PARTIAL_LINK_TEXT, "Sign up").click()
        WebDriverWait(fresh_driver, TIMEOUT).until(EC.url_contains("/signup"))
        assert "/signup" in fresh_driver.current_url


class TestSignup:
    """TC-AUTH-008 to TC-AUTH-011 — Signup page behaviour."""

    def test_signup_page_loads(self, fresh_driver):
        """Signup page renders with email, password, confirmPassword fields."""
        fresh_driver.get(f"{BASE_URL}/signup")
        assert find_and_wait(fresh_driver, By.NAME, "email")
        assert fresh_driver.find_element(By.NAME, "password").is_displayed()
        assert fresh_driver.find_element(By.NAME, "confirmPassword").is_displayed()

    def test_password_mismatch_shows_error(self, fresh_driver):
        """TC-AUTH-009: Mismatched passwords → 'Passwords don't match' error."""
        fresh_driver.get(f"{BASE_URL}/signup")
        wait = WebDriverWait(fresh_driver, TIMEOUT)
        wait.until(EC.presence_of_element_located((By.NAME, "email")))

        fresh_driver.find_element(By.NAME, "email").send_keys("newuser@example.com")
        fresh_driver.find_element(By.NAME, "password").send_keys("Password123!")
        fresh_driver.find_element(By.NAME, "confirmPassword").send_keys("DifferentPass!")
        fresh_driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        time.sleep(0.5)

        errors = fresh_driver.find_elements(By.CSS_SELECTOR, "p[id$='-message'], [role='alert']")
        messages = " ".join(e.text for e in errors if e.is_displayed())
        assert "match" in messages.lower() or "password" in messages.lower()

    def test_short_password_shows_error(self, fresh_driver):
        """TC-AUTH-010: Password < 6 chars → 'at least 6 characters' error."""
        fresh_driver.get(f"{BASE_URL}/signup")
        wait = WebDriverWait(fresh_driver, TIMEOUT)
        wait.until(EC.presence_of_element_located((By.NAME, "email")))

        fresh_driver.find_element(By.NAME, "email").send_keys("user@example.com")
        fresh_driver.find_element(By.NAME, "password").send_keys("abc")
        fresh_driver.find_element(By.NAME, "confirmPassword").send_keys("abc")
        fresh_driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        time.sleep(0.5)

        errors = fresh_driver.find_elements(By.CSS_SELECTOR, "p[id$='-message'], [role='alert']")
        messages = " ".join(e.text for e in errors if e.is_displayed())
        assert "6" in messages or "characters" in messages.lower()

    def test_duplicate_email_shows_error(self, fresh_driver):
        """TC-AUTH-011: Registering with existing email → duplicate error toast."""
        fresh_driver.get(f"{BASE_URL}/signup")
        wait = WebDriverWait(fresh_driver, TIMEOUT)
        wait.until(EC.presence_of_element_located((By.NAME, "email")))

        fresh_driver.find_element(By.NAME, "email").send_keys(TEST_EMAIL)
        fresh_driver.find_element(By.NAME, "password").send_keys(TEST_PASS)
        fresh_driver.find_element(By.NAME, "confirmPassword").send_keys(TEST_PASS)
        fresh_driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

        toast = wait.until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, "[data-sonner-toast], [role='alert']")
            )
        )
        assert "already" in toast.text.lower() or "use" in toast.text.lower()

    def test_login_link_on_signup_page(self, fresh_driver):
        """'Log in' link on signup page navigates back to /login."""
        fresh_driver.get(f"{BASE_URL}/signup")
        find_and_wait(fresh_driver, By.PARTIAL_LINK_TEXT, "Log in")
        fresh_driver.find_element(By.PARTIAL_LINK_TEXT, "Log in").click()
        WebDriverWait(fresh_driver, TIMEOUT).until(EC.url_contains("/login"))
        assert "/login" in fresh_driver.current_url


class TestForgotPassword:
    """TC-AUTH-012 — Forgot password page."""

    def test_forgot_password_page_loads(self, fresh_driver):
        """Forgot password page renders with email field and submit button."""
        fresh_driver.get(f"{BASE_URL}/forgot-password")
        assert find_and_wait(fresh_driver, By.NAME, "email")
        btn = fresh_driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        assert btn.is_displayed()

    def test_valid_email_triggers_success_message(self, fresh_driver):
        """TC-AUTH-012: Registered email → success feedback shown."""
        fresh_driver.get(f"{BASE_URL}/forgot-password")
        wait = WebDriverWait(fresh_driver, TIMEOUT)
        wait.until(EC.presence_of_element_located((By.NAME, "email")))

        fresh_driver.find_element(By.NAME, "email").send_keys(TEST_EMAIL)
        fresh_driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

        confirmation = wait.until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, "[data-sonner-toast], [role='status'], [role='alert']")
            )
        )
        assert confirmation.is_displayed()

    def test_invalid_email_format_on_forgot(self, fresh_driver):
        """Invalid email format on forgot password → inline validation error."""
        fresh_driver.get(f"{BASE_URL}/forgot-password")
        find_and_wait(fresh_driver, By.NAME, "email")

        fresh_driver.find_element(By.NAME, "email").send_keys("bademail")
        fresh_driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        time.sleep(0.5)

        errors = fresh_driver.find_elements(By.CSS_SELECTOR, "p[id$='-message'], [role='alert']")
        assert any(e.is_displayed() for e in errors)


class TestProtectedRoutes:
    """TC-AUTH-014 — Protected route redirect for unauthenticated users."""

    PROTECTED = ["/explore", "/articles", "/my-aquarium", "/compare", "/profile", "/nearby-aquariums"]

    @pytest.mark.parametrize("path", PROTECTED)
    def test_protected_route_redirects_to_login(self, fresh_driver, path):
        """Unauthenticated access to protected route → redirected to /login."""
        # Ensure no session cookies
        fresh_driver.delete_all_cookies()
        fresh_driver.get(f"{BASE_URL}{path}")

        wait = WebDriverWait(fresh_driver, TIMEOUT)
        wait.until(lambda d: "/login" in d.current_url or path in d.current_url)

        # Either redirected, or the page requires login
        url = fresh_driver.current_url
        if "/login" not in url:
            # Should at least show login prompt or be inaccessible
            login_indicators = fresh_driver.find_elements(By.CSS_SELECTOR, "button[type='submit']")
            has_login = any("sign in" in b.text.lower() for b in login_indicators)
            assert has_login or "/login" in url, f"Expected redirect to /login for {path}"
