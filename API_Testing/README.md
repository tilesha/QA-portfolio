# API Testing — Sample Notes

APIs often look like this in documentation:

`GET https://api.example.com/products?search=wireless`

✅ This is an **endpoint format example**:
- `api.example.com` is usually a placeholder domain in docs
- The response is typically **JSON**, not a web page
- Many APIs require authentication (token / API key)

## Sample Request (GET)
- Endpoint: `/products`
- Query param: `search=wireless`

## Example Mock Response (200 OK)
```json
{
  "items": [
    { "id": 101, "name": "Wireless Mouse", "price": 19.99 },
    { "id": 102, "name": "Wireless Keyboard", "price": 39.99 }
  ],
  "total": 2
}
```

## Basic API Test Scenarios
- [ ] 200 OK with valid search term
- [ ] Empty search returns default list (or 400 based on spec)
- [ ] Special characters in search (e.g., `%20`, `+`, `@`)
- [ ] Very long search string (boundary)
- [ ] Unauthorized request returns 401 (if auth is required)
