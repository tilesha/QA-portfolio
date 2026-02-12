## Summary  
User login attempt with expired password does not result in the expected error message. Instead, the login request fails silently or displays a generic "Invalid credentials" message, without directing the user to reset flow.

## Related Test Case  
[TC-LOGIN-104 – Login attempt with expired password](../Test_Cases/Web/Login_Form/Login_Negative.md#tc-login-104--login-attempt-with-expired-password)

## Steps to reproduce  
1. Ensure user account has expired password status  
2. Open login page  
3. Enter correct username and expired password  
4. Click “Login”  
5. Observe system response

## Expected Result  
System blocks login and shows specific error message:  
“Your password has expired. Reset required.”  
User is guided to recovery flow.

## Actual Result  
System shows generic “Invalid credentials” message or does not respond appropriately. No password reset prompt shown.

## Priority  
🟠 Medium

## Severity  
Moderate

## Status  
Selected for Development

## Environment  
- OS: Windows 11  
- Browser: Edge 116  
- Platform: Web App  
- Account: test_user_expired_pwd


## Labels  
Login, Password Expiry, UX, Functional

## Affected version  
v3.4.2

## Fix version  
none

## Reported On: 
July 30, 2025  

## Reported By: 
Ievgen  

## Assignee: 
Smith
