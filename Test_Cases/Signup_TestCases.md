# Signup — Test Cases (12)

**Environment**
- Platform: Web
- Browser: Chrome (latest)
- OS: Windows 10/11
- Network: Stable


| Test Case ID | Title | Preconditions | Steps | Expected Result | Priority |
| --- | --- | --- | --- | --- | --- |
| TC-SGN-001 | Signup with valid data | User is on signup page | Enter valid name, email, strong password, confirm, submit | Account created; user redirected/verified | High |
| TC-SGN-002 | Signup with already registered email | Email already exists | Enter existing email + other valid data, submit | Error: email already in use | High |
| TC-SGN-003 | Required fields validation | On signup page | Submit with all fields empty | Required validations shown | High |
| TC-SGN-004 | Invalid email format | On signup page | Enter invalid email, submit | Email format validation shown | Medium |
| TC-SGN-005 | Password strength rules | On signup page | Enter weak password, submit | Password rule message shown; block submit | High |
| TC-SGN-006 | Password and confirm mismatch | On signup page | Enter password != confirm, submit | Mismatch validation shown | High |
| TC-SGN-007 | Trim spaces in email input | On signup page | Enter email with spaces, submit | Spaces trimmed; validation uses trimmed value | Low |
| TC-SGN-008 | Name field accepts letters and spaces | On signup page | Enter name with spaces, submit | Accepted and stored correctly | Low |
| TC-SGN-009 | Max length validation | On signup page | Enter extremely long name/email, submit | Shows max length validation / prevents overflow | Medium |
| TC-SGN-010 | Terms & Conditions checkbox required | On signup page; T&C exists | Do not accept T&C, submit | Blocks submit and shows message | Medium |
| TC-SGN-011 | Email verification flow | Signup successful; verification enabled | Signup then check verification requirement | User prompted to verify email before full access | Medium |
| TC-SGN-012 | Accessibility: labels & error text | On signup page | Tab order, label presence, errors readable | Accessible labels and clear error messages | Low |
