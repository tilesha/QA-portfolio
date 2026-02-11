# API Testing (Sample)

These are **sample** API testing artifacts for practice.  
Note: links like `https://api.example.com/...` are often **placeholders** used in documentation.

## Sample Endpoint
`GET /products?search=wireless`

## Expected Response (Mock)
See `mock_products_response.json`

## Test Scenarios (10)
1. Valid search term returns matching products
2. Empty search term returns default list or validation error (per spec)
3. Special characters in search term handled safely
4. Very long search term handled (no 500 errors)
5. Case-insensitive search (if supported)
6. Pagination works (page, limit)
7. Sorting works (if supported)
8. Unauthorized request returns 401 (if auth required)
9. Rate limit returns 429 after threshold
10. Server error returns meaningful message (5xx handling)
