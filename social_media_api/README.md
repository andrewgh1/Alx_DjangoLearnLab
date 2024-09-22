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

## Implementing User Follows and Feed Functionality
## mandatory
Objective: Expand the Social Media API by adding features for users to follow other users and view an aggregated feed of posts from users they follow. This task enhances the social aspect of the platform, mimicking key functionalities seen in popular social media networks.

## Task Description:
In this task, you will build on your existing social_media_api by incorporating user relationships and a dynamic content feed. This involves managing user follow relationships and creating a feed that displays posts from followed users.

Step 1: Update the User Model to Handle Follows
Model Adjustments:
Modify your custom user model to include a following field, which is a many-to-many relationship to itself, representing the users that a given user follows.
Make necessary migrations to update the user model: bash python manage.py makemigrations accounts python manage.py migrate
Step 2: Create API Endpoints for Managing Follows
Follow Management Views:
Develop views in the accounts app that allow users to follow and unfollow others. This might include actions like follow_user and unfollow_user, which update the following relationship.
Ensure proper permissions are enforced so users can only modify their own following list.
Step 3: Implement the Feed Functionality
Feed Generation:
Create a view in the posts app that generates a feed based on the posts from users that the current user follows.
This view should return posts ordered by creation date, showing the most recent posts at the top.
Step 4: Define URL Patterns for New Features
Routing for Follows and Feed:
Set up URL patterns in accounts/urls.py for follow management (e.g., /follow/<int:user_id>/ and /unfollow/<int:user_id>/).
Add a route in posts/urls.py for the feed endpoint, such as /feed/.
Step 5: Test Follow and Feed Features
Testing and Validation:
Conduct thorough tests to ensure that the follow system works as intended and that the feed correctly displays posts from followed users.
Use Postman or similar tools to simulate the user experience and verify the correctness of the output.
Step 6: Documentation
API Documentation:
Update your project documentation to include details on how to manage follows and access the feed. Provide clear instructions and examples for each new endpoint.
Document any changes made to models, especially modifications to the user model.
Deliverables:
Updated Models and Migrations: Include changes to the user model and any new migrations.
Code Files for Views and Serializers: Implementations for follow management and feed generation.
URL Configurations: New routes added for managing follows and retrieving the feed.
Documentation: Comprehensive API documentation covering the new functionalities.
Repo:

GitHub repository: Alx_DjangoLearnLab
Directory: social_media_api

# Social Media API Documentation for Notification Endpoints

This project is a Django-based Social Media API with user authentication, posts, comments, user follows, feed functionality, likes, and notifications.

## Setup

(Previous setup instructions remain the same)

## API Endpoints

(Previous endpoints for User Registration, Login, Posts, Comments, and User Follows remain the same)

### Likes

- Like a Post
  - URL: `/api/posts/{post_id}/like/`
  - Method: POST
  - Authentication: Required
  - Response: Confirmation message

- Unlike a Post
  - URL: `/api/posts/{post_id}/unlike/`
  - Method: POST
  - Authentication: Required
  - Response