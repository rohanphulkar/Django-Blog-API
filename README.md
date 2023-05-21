# Django Blog API

The Django Blog API is a RESTful web service that provides backend functionality for a blog application. It is built using Django, a powerful Python web framework, and utilizes various Django packages and libraries to implement essential features.

## Project Structure

The project follows a modular structure with separate apps for user accounts and blog posts. The main components include:

- **accounts**: Manages user authentication, account registration, email verification, and user-related functionalities.
- **posts**: Handles blog post creation, retrieval, modification, and deletion, as well as comment management and category handling.
- **requirements.txt**: Lists all the Python packages required for running the project.

## Features

- User registration and authentication
- Create, read, update, and delete blog posts
- Add comments to blog posts
- Retrieve blog posts by category or author
- Search blog posts by title or content
- Token-based authentication using JWT (JSON Web Tokens)

## Tech Used

- Django: ![Django](https://res.cloudinary.com/rohanphulkar/image/upload/v1684620096/social-icons/django-logo-positive_owriys.svg)

- Gunicorn: ![Gunicorn](https://res.cloudinary.com/rohanphulkar/image/upload/v1684619768/social-icons/gunicorn-ar21_n9i04d.svg)

- MySQL: ![Mysql](https://res.cloudinary.com/rohanphulkar/image/upload/v1684620421/social-icons/mysql-official_uh7mlm.svg)

## API Endpoints

- `POST /accounts/register/`: Register a new user.
- `POST /accounts/login/`: Obtain a JWT access token.
- `GET /posts/`: Retrieve all blog posts.
- `POST /posts/`: Create a new blog post.
- `GET /posts/{post_id}/`: Retrieve a specific blog post.
- `PUT /posts/{post_id}/`: Update a specific blog post.
- `DELETE /posts/{post_id}/`: Delete a specific blog post.
- `GET /posts/{post_id}/comments/`: Retrieve all comments for a specific blog post.
- `POST /posts/{post_id}/comments/`: Add a new comment to a specific blog post.

## Installation and Setup

To run the Django Blog API locally, follow these steps:

1. Clone the repository:

```
git clone https://github.com/rohanphulkar/django-blog-api.git
```

2. Navigate to the project directory:

```
cd django-blog-api
```

3. Create and activate a virtual environment (recommended):

- Create: `python -m venv env`

- Activate:
  - Windows: `.\env\Scripts\activate`
  - Unix/Mac: `source env/bin/activate`

4. Install the required packages:

```
pip install -r requirements.txt
```

5. Apply database migrations:

```
python manage.py migrate
```

6. Start the development server:

```
python manage.py runserver
```

## Credits

The Django Blog API project is developed and maintained by [Rohan Phulkar](https://github.com/rohanphulkar).

- 👨‍💻 All of my projects are available at [rohanphulkar.vercel.app](rohanphulkar.vercel.app)
- LinkedIn: [![rohanphulkar](https://res.cloudinary.com/rohanphulkar/image/upload/v1684619255/social-icons/linked-in-alt_dsqxqx.svg)](https://linkedin.com/in/rohanphulkar)

- Instagram: [![codes.rohan](https://res.cloudinary.com/rohanphulkar/image/upload/v1684619255/social-icons/instagram_slovbx.svg)](https://instagram.com/codes.rohan)
