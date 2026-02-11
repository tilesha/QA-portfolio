-- SQL Validation Samples

-- 1) Find user by email
SELECT id, email, status
FROM users
WHERE email = 'user@example.com';

-- 2) Validate latest login record
SELECT user_id, created_at, ip_address
FROM login_audit
WHERE user_id = 123
ORDER BY created_at DESC
LIMIT 1;
