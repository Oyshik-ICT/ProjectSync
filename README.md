# Project Management API

A RESTful API built with Django REST Framework for managing projects, tasks, and comments. The API allows users to create projects, assign tasks, and collaborate through comments.

## Features

- JWT Authentication
- User authentication and authorization
- Project management with ownership
- Task management with status and priority tracking
- Comment system for tasks
- RESTful API endpoints

## Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Virtual environment (recommended)

## Installation & Setup

1. Clone the repository:
```bash
git clone https://github.com/Oyshik-ICT/ProjectSync.git
cd ProjectSync/
```

2. Create and activate a virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Apply database migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```

5. Create a superuser (admin):
```bash
python manage.py createsuperuser
```

6. Run the development server:
```bash
python manage.py runserver
```

The API will be available at `http://localhost:8000/`.

## Authentication

This API uses JWT (JSON Web Token) authentication. Here's how to authenticate:

1. **Obtain JWT Token**:
```bash
POST /token/
{
    "username": "your_username",
    "password": "your_password"
}
```
Response:
```json
{
    "refresh": "your_refresh_token",
    "access": "your_access_token"
}
```

2. **Use the Token**:
Add the access token to your request headers:
```
Authorization: Bearer your_access_token
```

3. **Refresh Token**:
When the access token expires, use the refresh token to get a new access token:
```bash
POST /token/refresh/
{
    "refresh": "your_refresh_token"
}
```

## API Endpoints

### User Management
- `POST /users/` - Register new user (public)
- `GET /users/` - List users (authenticated)
- `GET /users/{id}/` - Get user details (authenticated)
- `PUT/PATCH /users/{id}/` - Update user (authenticated)
- `DELETE /users/{id}/` - Delete user (authenticated)

### Projects
- `GET /projects/` - List user's projects
- `POST /projects/` - Create new project
- `GET /projects/{id}/` - Get project details
- `PUT/PATCH /projects/{id}/` - Update project
- `DELETE /projects/{id}/` - Delete project

### Tasks
- `GET /projects/{project_pk}/tasks/` - List tasks in project
- `POST /projects/{project_pk}/tasks/` - Create new task
- `GET /projects/{project_pk}/tasks/{pk}/` - Get task details
- `PUT/PATCH /projects/{project_pk}/tasks/{pk}/` - Update task
- `DELETE /projects/{project_pk}/tasks/{pk}/` - Delete task

### Comments
- `GET /tasks/{task_pk}/comments/` - List comments on task
- `POST /tasks/{task_pk}/comments/` - Create new comment
- `GET /tasks/{task_pk}/comments/{pk}/` - Get comment details
- `PUT/PATCH /tasks/{task_pk}/comments/{pk}/` - Update comment
- `DELETE /tasks/{task_pk}/comments/{pk}/` - Delete comment

## Using the API with Postman

1. **Authentication**:
   - Register a new user using `POST /users/`
   - Obtain JWT token using `POST /token/`
   - Add the token to your request headers: `Authorization: Bearer your_access_token`
   - For protected endpoints, make sure to include the JWT token in the header

2. **Sample Request Bodies**:

   Create User:
   ```json
   {
       "username": "testuser",
       "password": "your_password",
       "email": "test@example.com",
       "first_name": "Test",
       "last_name": "User"
   }
   ```

   Create Project:
   ```json
   {
       "name": "New Project",
       "description": "Project description",
       "owner": 1
   }
   ```

   Create Task:
   ```json
   {
       "title": "New Task",
       "description": "Task description",
       "status": "To Do",
       "priority": "Medium",
       "assign_to": 1,
       "project": 1,
       "due_date": "2024-12-31T23:59:59Z"
   }
   ```

   Create Comment:
   ```json
   {
       "content": "This is a comment",
       "user": 1,
       "task": 1
   }
   ```


