# Project
Problem Statement: Create a simple web application that allows users to sign up, log in, and upload images. Implement basic authentication and authorization mechanisms to ensure secure access to user data.

# My Django Image Upload Application

This is a simple Django web application that allows users to sign up, log in, and upload images. It implements basic authentication and authorization mechanisms to ensure secure access to user data.

## Installation and Setup

1. **Clone the repository:**
git clone <repository_url>
cd my_django_image_upload_app

2. **Install dependencies:**
pip install -r requirements.txt 
3. **Apply migrations:**
4. **Create a superuser:**
python manage.py createsuperuser

5. **Run the development server:**
python manage.py runserver

6. **Access the application in your web browser at:** `http://127.0.0.1:8000/`

## Usage

### User Registration

1. **Navigate to the registration page:**
http://127.0.0.1:8000/accounts/register/

2. **Fill out the registration form with your desired username and password.**

### User Login

1. **Navigate to the login page:**
http://127.0.0.1:8000/accounts/login/

2. **Enter your username and password.**

### Image Upload

1. **After logging in, you can access the image upload page:**
http://127.0.0.1:8000/upload/

2. **Choose an image file using the provided form and click the "Upload" button.**

### Accessing Admin Panel

1. **Navigate to the admin panel:**
http://127.0.0.1:8000/admin/

2. **Log in using the superuser credentials created during setup.**

## Additional Information

- Make sure to configure the `MEDIA_URL` and `MEDIA_ROOT` settings in your `settings.py` file to handle uploaded images.
- This application uses Django's built-in authentication system. You can customize the authentication templates and views as needed.
- Ensure that the `DIRS` option in the `TEMPLATES` configuration in `settings.py` includes the path to your project's templates directory.




