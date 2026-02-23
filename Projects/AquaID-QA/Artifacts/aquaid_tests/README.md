# 🐟 AquaID — Selenium & API Test Suite

Automated test suite for the **AquaID** freshwater fish identification web app.  
Written in **Python + Selenium WebDriver** for UI tests, and **requests** for direct API tests.

---

## 📁 Project Structure

```
aquaid_tests/
├── conftest.py                          # Shared fixtures & helpers (driver, login, wait)
├── pytest.ini                           # pytest configuration & markers
├── requirements.txt                     # Python dependencies
├── fixtures/
│   ├── fish_sample.jpg                  # ← ADD: valid fish photo for upload tests
│   ├── landscape.jpg                    # ← ADD: non-fish photo for negative tests
│   └── large_image.jpg                  # ← ADD: >5MB image for size limit tests
├── tests/
│   ├── test_auth.py                     # Login, Signup, Forgot Password, Protected Routes
│   ├── test_fish_identification.py      # Image upload & AI identification flow
│   ├── test_my_aquarium.py              # Aquarium CRUD: view, add, edit, filter, remove
│   └── test_compare_and_articles.py     # Compare Fish + Explore & Articles
└── api_tests/
    └── test_api_endpoints.py            # Direct HTTP tests for all API endpoints
```

---

## ⚙️ Setup

### 1. Install Python dependencies
```bash
cd aquaid_tests
pip install -r requirements.txt
```

### 2. Install ChromeDriver
`webdriver-manager` installs it automatically, OR install manually:
```bash
# Check Chrome version
google-chrome --version

# Download matching ChromeDriver from:
# https://chromedriver.chromium.org/downloads
```

### 3. Add test fixtures
Place real image files in the `fixtures/` folder:
- `fish_sample.jpg` — A clear photo of a freshwater fish (e.g. Guppy, Betta)
- `landscape.jpg` — A non-fish image (for negative tests)
- `large_image.jpg` — Any image > 5MB (for file size validation tests)

### 4. Set environment variables

```bash
# App URLs
export AQUAID_URL="http://localhost:5173"      # Vite dev server
export AQUAID_API="http://localhost:5000/api"  # Express API server

# Test credentials (create these accounts in Firebase first)
export TEST_EMAIL="your.qa.account@gmail.com"
export TEST_PASS="YourTestPassword123!"
export TEST_EMAIL2="your.qa.account2@gmail.com"   # For cross-user tests
export TEST_PASS2="YourTestPassword456!"

# Firebase ID token (for API tests — get from browser DevTools)
# Open DevTools > Console > run: await firebase.auth().currentUser.getIdToken()
export FIREBASE_TOKEN="eyJhbGci..."
export FIREBASE_TOKEN2="eyJhbGci..."           # Second user's token

# Optional: show browser during tests (default: headless)
export HEADLESS=false
```

---

## ▶️ Running Tests

### Run all tests
```bash
cd aquaid_tests
pytest
```

### Run Selenium UI tests only
```bash
pytest tests/ -v
```

### Run API tests only (no browser)
```bash
pytest api_tests/ -v
```

### Run a specific module
```bash
pytest tests/test_auth.py -v
pytest tests/test_my_aquarium.py -v
pytest tests/test_compare_and_articles.py -v
```

### Run by marker
```bash
pytest -m auth        # Auth tests only
pytest -m api         # API tests only
pytest -m "not slow"  # Skip slow AI tests
```

### Generate HTML report
```bash
pytest --html=report.html --self-contained-html
```

---

## 🧪 Test Coverage Summary

| Module | File | Tests |
|---|---|---|
| Authentication | `test_auth.py` | 18 tests |
| Fish Identification | `test_fish_identification.py` | 9 tests |
| My Aquarium | `test_my_aquarium.py` | 14 tests |
| Compare Fish | `test_compare_and_articles.py` | 11 tests |
| Explore & Articles | `test_compare_and_articles.py` | 12 tests |
| API Endpoints | `test_api_endpoints.py` | 30 tests |
| **Total** | | **~94 tests** |

---

## 🔐 Getting a Firebase Token (for API tests)

1. Start the AquaID app locally
2. Log in with your test account
3. Open browser DevTools (F12) → Console
4. Run:
   ```js
   const token = await firebase.auth().currentUser.getIdToken(true);
   console.log(token);
   ```
5. Copy the token and set it as `FIREBASE_TOKEN`

Tokens expire after 1 hour — regenerate if tests start returning 401.

---

## ⚠️ Known Issues (from Bug Reports)

| Bug | Test | Expected | Current |
|---|---|---|---|
| DELETE article not implemented | `test_delete_article_endpoint_not_implemented` | 200 + deleted | 200 but not deleted |
| No file type validation | `test_non_image_file_handled` | 400 | 500 |
| >5MB files not rejected | `test_large_file_rejected` | 413 | 500 |
| Same fish compared to itself | `test_compare_same_id_returns_200_but_no_validation` | 400 | 200 |

---

## 📝 Notes

- Tests in `test_fish_identification.py` that upload images require the `fixtures/` files.
- AI identification tests may take 10–30 seconds (Gemini API response time).
- Rate limit test (`test_tts_rate_limit_enforced`) sends 6 TTS requests — use a dedicated test account.
- Some Selenium tests use `pytest.skip()` when preconditions aren't met (e.g. no fish in aquarium).
