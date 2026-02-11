# Login — Test Cases (20)

**Environment**
- Platform: Web
- Browser: Chrome (latest)
- OS: Windows 10/11
- Network: Stable


| Test Case ID | Title | Preconditions | Steps | Expected Result | Priority |
| --- | --- | --- | --- | --- | --- |
| TC-LGN-001 | Login with valid credentials | User is registered | Enter valid email+password, click Login | User logged in and redirected to dashboard/home | High |
| TC-LGN-002 | Login with invalid password | User is registered | Enter valid email + wrong password, click Login | Error shown; user not logged in | High |
| TC-LGN-003 | Login with unregistered email | None | Enter unregistered email + any password, click Login | Error shown; no login | High |
| TC-LGN-004 | Empty email and password | On login page | Click Login without entering anything | Required field validation shown | High |
| TC-LGN-005 | Empty email only | On login page | Leave email empty, enter password, click Login | Email required validation shown | Medium |
| TC-LGN-006 | Empty password only | On login page | Enter email, leave password empty, click Login | Password required validation shown | Medium |
| TC-LGN-007 | Invalid email format | On login page | Enter 'abc@', any password, click Login | Email format validation shown | Medium |
| TC-LGN-008 | Trim spaces in email | On login page | Enter email with leading/trailing spaces + valid password, login | Spaces trimmed; login succeeds | Medium |
| TC-LGN-009 | Password masking | On login page | Type password | Password characters masked | Low |
| TC-LGN-010 | Show/Hide password toggle | On login page | Toggle eye icon | Password visibility toggles correctly | Low |
| TC-LGN-011 | Remember me keeps session | On login page | Tick Remember me, login, close & reopen browser, revisit site | User remains logged in (per requirement) | Medium |
| TC-LGN-012 | Remember me off ends session | On login page | Do not tick Remember me, login, close browser, reopen | User is logged out (per requirement) | Medium |
| TC-LGN-013 | Account lock after multiple failures | User exists; policy configured | Enter wrong password 5 times | Account temporarily locked or captcha triggered | High |
| TC-LGN-014 | Error message does not reveal which field is wrong | On login page | Try invalid credentials | Generic error like 'Invalid credentials' | Medium |
| TC-LGN-015 | Login button disabled until valid inputs | On login page | Observe button state while typing invalid/valid values | Button enables only when inputs valid (if designed) | Low |
| TC-LGN-016 | Press Enter submits form | On login page | Enter valid creds, press Enter | Form submitted; login works | Low |
| TC-LGN-017 | Back button after login | Logged in | Login then press browser Back | User stays logged in; no sensitive data leakage | Low |
| TC-LGN-018 | Logout clears session | Logged in | Click Logout, revisit protected page URL | Redirect to login; session cleared | High |
| TC-LGN-019 | Rate limiting / brute force protection | On login page | Attempt many logins quickly | Requests throttled / captcha / temporary block | Medium |
| TC-LGN-020 | Accessibility: focus order and labels | On login page | Tab through fields; screen reader labels | Logical focus order; labels announced | Low |
