# Blog Project

## Overview

This is a Django-based blog project that allows users to create, read, update, and delete blog posts. The project includes user authentication, API integration using Django REST Framework (DRF), and JWT-based authentication for secure access to API endpoints.

## Features

- User authentication (Login, Registration, JWT Authentication)
- Create, read, update, and delete (CRUD) blog posts
- REST API endpoints for blog post management
- Secure authentication using JWT (JSON Web Token)
- Template-based rendering for frontend views
- Admin panel for managing users and blog posts

## Technologies Used

- **Backend:** Django, Django REST Framework (DRF)
- **Authentication:** JWT (JSON Web Token)
- **Database:** SQLite3/MySQL
- **Frontend:** HTML, CSS, Bootstrap
- **Tools:** Git, Postman

## Installation

1. Clone the repository:

   ```sh
   git clone <repository_url>
   cd blog_project
   ```

2. Create and activate a virtual environment:

   ```sh
   python -m venv venv
   source venv/bin/activate  # On macOS/Linux
   venv\Scripts\activate  # On Windows
   ```

3. Install dependencies:

   ```sh
   pip install -r requirements.txt
   ```

4. Apply database migrations:

   ```sh
   python manage.py migrate
   ```

5. Create a superuser (for admin access):

   ```sh
   python manage.py createsuperuser
   ```

6. Run the development server:

   ```sh
   python manage.py runserver
   ```

7. Access the application at `http://127.0.0.1:8000/`

## API Endpoints

The blog project includes REST API endpoints for managing blog posts.

- **Authentication:**

  - `POST /api/token/` (Obtain JWT token)
  - `POST /api/token/refresh/` (Refresh JWT token)

- **Blog Posts:**

  - `GET /api/posts/` (Retrieve all posts)
  - `POST /api/posts/` (Create a new post)
  - `GET /api/posts/<id>/` (Retrieve a single post)
  - `PUT /api/posts/<id>/` (Update a post)
  - `DELETE /api/posts/<id>/` (Delete a post)

## Usage

- Users can register and log in to create and manage their blog posts.
- API endpoints can be tested using Postman or any API testing tool.
- Admins can manage posts and users from the Django admin panel (`/admin`).

## License

This project is open-source and available under the MIT License.

## Author

Subash Chandra Bose

