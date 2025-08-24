# API Interface Design Guidelines

## URL Structure Patterns

### Resource-Based URLs
```
{base_url}/{resource}/{identifier}
{base_url}/{resource}/{identifier}/{sub_resource}
```
**Examples:**
- `GET /api/books/123` - Get book with ID 123
- `GET /api/books/123/reviews` - Get reviews for book 123
- `POST /api/users/456/orders` - Create order for user 456

### Anti-Pattern: Avoid RPC-style URLs
❌ **Don't do this:**
- `GET /api/getbook?id=123`
- `POST /api/createUser`
- `DELETE /api/deleteBook/123`

✅ **Do this instead:**
- `GET /api/books/123`
- `POST /api/users`
- `DELETE /api/books/123`

## HTTP Methods

| Method | Purpose | Example |
|--------|---------|---------|
| GET | Retrieve resource(s) | `GET /api/books` |
| POST | Create new resource | `POST /api/books` |
| PUT | Update/replace entire resource | `PUT /api/books/123` |
| PATCH | Partial update | `PATCH /api/books/123` |
| DELETE | Remove resource | `DELETE /api/books/123` |

## JSON Response Structure

### Standard Response Format
```json
{
  "success": true,
  "data": {
    "id": 123,
    "title": "Clean Code",
    "author": "Robert Martin",
    "published_year": 2008
  },
  "message": "Book retrieved successfully",
  "timestamp": "2023-10-01T12:00:00Z"
}
```

### Error Response Format
```json
{
  "success": false,
  "error": {
    "code": "BOOK_NOT_FOUND",
    "message": "Book with ID 123 not found",
    "details": {
      "requested_id": 123,
      "available_ids": [1, 2, 5, 10]
    }
  },
  "timestamp": "2023-10-01T12:00:00Z"
}
```

### Collection Response Format
```json
{
  "success": true,
  "data": {
    "items": [
      {"id": 1, "title": "Book 1"},
      {"id": 2, "title": "Book 2"}
    ],
    "pagination": {
      "page": 1,
      "limit": 10,
      "total": 25,
      "has_next": true
    }
  }
}
```

## Core Design Principles

### 1. Statelessness
Each request must contain all information needed to process it. The server should not rely on stored context from previous requests.

**Implementation:**
- Include authentication tokens in headers
- Pass all required parameters in the request
- Don't rely on server-side sessions for API state

**Example:**
```http
GET /api/books?page=2&limit=10
Authorization: Bearer eyJhbGciOiJIUzI1NiIs...
Content-Type: application/json
```

### 2. Resource-Based Design
Structure URLs around resources (nouns) rather than actions (verbs).

**Good Resource Hierarchy:**
```
/api/books/{book_id}
/api/books/{book_id}/chapters
/api/books/{book_id}/chapters/{chapter_id}
/api/authors/{author_id}
/api/authors/{author_id}/books
```

### 3. Consistent Naming Conventions
- Use lowercase letters
- Use hyphens for multi-word resources
- Use plural nouns for collections
- Use consistent field naming (snake_case or camelCase)

## Status Codes

### Success Codes
- `200 OK` - Successful GET, PUT, PATCH
- `201 Created` - Successful POST
- `204 No Content` - Successful DELETE

### Client Error Codes
- `400 Bad Request` - Invalid request format
- `401 Unauthorized` - Authentication required
- `403 Forbidden` - Access denied
- `404 Not Found` - Resource doesn't exist
- `422 Unprocessable Entity` - Validation errors

### Server Error Codes
- `500 Internal Server Error` - Unexpected server error
- `502 Bad Gateway` - Upstream service error
- `503 Service Unavailable` - Temporary overload