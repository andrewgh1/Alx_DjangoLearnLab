## Social Media API User Creation And Authentication

This project is a Django-based Social Media API with user authentication functionality.

## Setup

1. Clone the repository:
   ```
   git clone https://github.com/your-username/Alx_DjangoLearnLab.git
   cd Alx_DjangoLearnLab/social_media_api
   ```

2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Apply migrations:
   ```
   python manage.py makemigrations
   python manage.py migrate
   ```

4. Run the development server:
   ```
   python manage.py runserver
   ```

## API Endpoints

### User Registration
- URL: `/api/accounts/register/`
- Method: POST
- Data Params: 
  ```json
  {
    "username": "string",
    "password": "string",
    "password2": "string",
    "email": "string",
  }
  ```
- Success Response: 
  - Code: 201
  - Content: `{ "user_id": 1, "username": "string", "token": "string" }`

### User Login
- URL: `/api/accounts/login/`
- Method: POST
- Data Params:
  ```json
  {
    "username": "string",
    "password": "string"
  }
  ```
- Success Response:
  - Code: 200
  - Content: `{ "user_id": 1, "username": "string", "token": "string" }`

## User Model

The custom user model extends Django's AbstractUser and includes the following additional fields:
- `bio`: TextField
- `profile_picture`: ImageField
- `followers`: ManyToManyField (self-referential)
- `following`: ManyToManyField (self-referential)

## Authentication

This API uses Token Authentication. Include the token in the Authorization header for protected routes:
```
Authorization: Token <your-token-here>
```

## Testing

Use tools like Postman or cURL to test the API endpoints. Ensure you're using the correct URL, method, and data format as specified in the API documentation.

# Social Media Posts and Comments Functionality

This project is a Django-based Social Media API with user authentication, posts, and comments functionality.

## Setup

(Previous setup instructions remain the same)

## API Endpoints

### User Registration and Login

(Previous user registration and login endpoints remain the same)

### Posts

- List/Create Posts
  - URL: `/api/posts/`
  - Methods: GET, POST
  - Authentication: Required for POST
  - GET Response: List of posts (paginated)
  - POST Data Params:
    ```json
    {
      "title": "string",
      "content": "string"
    }
    ```

- Retrieve/Update/Delete Post
  - URL: `/api/posts/{id}/`
  - Methods: GET, PUT, PATCH, DELETE
  - Authentication: Required for PUT, PATCH, DELETE (must be the author)
  - PUT/PATCH Data Params:
    ```json
    {
      "title": "string",
      "content": "string"
    }
    ```

### Comments

- List/Create Comments
  - URL: `/api/comments/`
  - Methods: GET, POST
  - Authentication: Required for POST
  - GET Response: List of comments (paginated)
  - POST Data Params:
    ```json
    {
      "post": "int",
      "content": "string"
    }
    ```

- Retrieve/Update/Delete Comment
  - URL: `/api/comments/{id}/`
  - Methods: GET, PUT, PATCH, DELETE
  - Authentication: Required for PUT, PATCH, DELETE (must be the author)
  - PUT/PATCH Data Params:
    ```json
    {
      "content": "string"
    }
    ```

## Pagination

All list endpoints are paginated. Use `?page=<page_number>` to navigate through pages.

## Filtering Posts

You can search posts by title or content using the `search` query parameter:

```
GET /api/posts/?search=<search_term>
```

## Authentication

This API uses Token Authentication. Include the token in the Authorization header for protected routes:
```
Authorization: Token <your-token-here>
```

## Testing

Run the tests using:
```
python manage.py test
```

For manual testing, use tools like Postman or cURL to interact with the API endpoints.