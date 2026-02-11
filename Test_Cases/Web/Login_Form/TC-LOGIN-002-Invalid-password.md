## TC-LOGIN-002 — Login fails with invalid password

**Module:** Web > Login  
**Type:** Functional / UI  
**Priority:** High / Medium / Low  
**Preconditions:** User account exists.

### Steps
1. Open the login page
2. Enter a valid email and an invalid password
3. Click **Login**

### Test Data
- Email: user@example.com / Password: WrongPass!

### Expected Result
- An error message is shown and user stays on login page; no session is created.

### Notes
- Verify error text, UI state, and that password field masking works.
