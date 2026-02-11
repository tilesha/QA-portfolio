# Forgot Password — Test Cases (8)

**Environment**
- Platform: Web
- Browser: Chrome (latest)
- OS: Windows 10/11
- Network: Stable


| Test Case ID | Title | Preconditions | Steps | Expected Result | Priority |
| --- | --- | --- | --- | --- | --- |
| TC-FPW-001 | Request reset with registered email | Email exists | Enter registered email, submit | Success message; reset email sent | High |
| TC-FPW-002 | Request reset with unregistered email | Email not registered | Enter unregistered email, submit | Generic success message (no account disclosure) | High |
| TC-FPW-003 | Empty email validation | On forgot password page | Submit with empty email | Email required validation shown | High |
| TC-FPW-004 | Invalid email format validation | On forgot password page | Enter invalid email format, submit | Email format validation shown | Medium |
| TC-FPW-005 | Reset link expires | Reset link issued | Open link after expiry time | Shows expired link message; request new link | Medium |
| TC-FPW-006 | Reset password meets policy | On reset password page | Enter new password meeting policy, submit | Password updated; can login with new password | High |
| TC-FPW-007 | Reset password mismatch validation | On reset password page | New password != confirm, submit | Mismatch validation shown | High |
| TC-FPW-008 | Rate limiting reset requests | On forgot password page | Request reset many times quickly | Throttled / limited; message shown | Medium |
