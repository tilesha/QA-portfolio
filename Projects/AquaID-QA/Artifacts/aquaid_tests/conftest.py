"""
AquaID – Selenium Test Suite
conftest.py – Shared fixtures used across all test modules
"""

import pytest
import time
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# ── Config ────────────────────────────────────────────────────────────────────
BASE_URL   = os.getenv("AQUAID_URL",  "http://localhost:5173")
API_URL    = os.getenv("AQUAID_API",  "http://localhost:5000/api")
TEST_EMAIL = os.getenv("TEST_EMAIL",  "tilesha.qa.test@gmail.com")
TEST_PASS  = os.getenv("TEST_PASS",   "TestPassword123!")
TEST_EMAIL2 = os.getenv("TEST_EMAIL2","tilesha.qa.test2@gmail.com")
TEST_PASS2  = os.getenv("TEST_PASS2", "TestPassword456!")
TIMEOUT     = 15  # seconds

# ── Driver fixture ────────────────────────────────────────────────────────────
@pytest.fixture(scope="session")
def driver():
    """
    Shared Chrome WebDriver for the entire test session.
    Runs headless by default; set HEADLESS=false to see the browser.
    """
    options = Options()
    if os.getenv("HEADLESS", "true").lower() != "false":
        options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1440,900")
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-popup-blocking")

    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(5)
    yield driver
    driver.quit()


@pytest.fixture(scope="function")
def fresh_driver():
    """Per-test isolated driver (slower but cleaner state)."""
    options = Options()
    if os.getenv("HEADLESS", "true").lower() != "false":
        options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1440,900")
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(5)
    yield driver
    driver.quit()


# ── Helper: wait util ─────────────────────────────────────────────────────────
@pytest.fixture(scope="session")
def wait(driver):
    return WebDriverWait(driver, TIMEOUT)


# ── Helper: login ─────────────────────────────────────────────────────────────
@pytest.fixture(scope="session")
def logged_in(driver, wait):
    """Log in once at session start; reuse across tests."""
    driver.get(f"{BASE_URL}/login")
    wait.until(EC.presence_of_element_located((By.NAME, "email")))

    driver.find_element(By.NAME, "email").send_keys(TEST_EMAIL)
    driver.find_element(By.NAME, "password").send_keys(TEST_PASS)
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    wait.until(EC.url_contains("/"))
    time.sleep(1)
    return driver


# ── Helper: navigate ──────────────────────────────────────────────────────────
def navigate(driver, path):
    driver.get(f"{BASE_URL}{path}")
    time.sleep(0.8)


def find_and_wait(driver, by, selector, timeout=TIMEOUT):
    return WebDriverWait(driver, timeout).until(
        EC.presence_of_element_located((by, selector))
    )


def click_and_wait(driver, by, selector, timeout=TIMEOUT):
    el = WebDriverWait(driver, timeout).until(
        EC.element_to_be_clickable((by, selector))
    )
    el.click()
    return el


def get_toast_text(driver, timeout=TIMEOUT):
    """Return text of the first visible toast notification."""
    toast = WebDriverWait(driver, timeout).until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, "[data-sonner-toast], [data-radix-toast-viewport] li")
        )
    )
    return toast.text
