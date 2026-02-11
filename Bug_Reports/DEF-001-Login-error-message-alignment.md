## Summary
Login error message overlaps the password input field on small screens.

## Related Test Case
[TC-LOGIN-002 — Login fails with invalid password](../Test_Cases/Web/Login_Form/TC-LOGIN-002-Invalid-password.md)

## Steps to reproduce
1. Open the login page on a 360×800 viewport (mobile size)
2. Enter valid email + invalid password
3. Tap **Login**

## Expected Result
Error message appears below the password field without overlapping UI elements.

## Actual Result
Error message overlaps the password input; user cannot clearly see the field state.

## Priority
🟡 Low

## Severity
Minor

## Status
Open

## Environment
- OS: Windows 11
- Browser/App: Chrome (Responsive mode)
- Platform: Web
- Build/Version: v1.0 (demo)

## Attachments
- Screenshot/Video: (add link or screenshot here)
- Logs: N/A

## Labels
UI, Responsive

## Reported On
February 11, 2026

## Reported By
Tilesha
