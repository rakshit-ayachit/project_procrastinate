# Project Procrastinate -  Django App - [Quick Start Guide]

This guide will walk you through the steps to set up and run a Django web application from this GitHub repository.

## Introduction

This guide will help you get a Django application up and running as quickly as possible.

## Prerequisites

Before you get started, make sure you have the following prerequisites installed on your system:

- **Python**: You can download Python from the [official Python website](https://www.python.org/downloads/).
- **Git**: To clone the repository, you'll need Git. You can download it from [here](https://git-scm.com/downloads).

## Installation

1. **Clone the Repository**: Open your terminal or command prompt and navigate to the directory where you want to clone the repository. Then, run the following command:

   ```bash
   git clone https://github.com/rakshit-ayachit/project_procrastinate.git

2. **Navigate to the project directory**:
   ```bash
   cd django_running_app/
3. **Create a virtual environment**: 
   ```bash
   python3 -m venv test

4. **Activate the virtual environment**:
- On Windows:
   ```bash
  test\Scripts\activate
- On macOS and Linux:
   ```bash
  source test/bin/activate
   ```

5. **Install Dependencies**:Navigate to the project directory and use Pip to install the project's dependencies listed in the requirements.txt file (if available). Run the following command:
    ```bash
    pip install -r requirements.txt
6. **Configure Settings**: Django apps may require specific settings like database configurations and secret keys. Ensure that you configure the project according to your environment. You can create a settings_local.py file for this purpose or modify the settings.py file directly.
7. **Apply Migrations**: If the app uses a database, apply the necessary database migrations to create tables:
   ```bash
   python manage.py makemigrations
   python manage.py migrate

8. **Create Superuser**:  If the app includes an admin panel, you can create a superuser account to access the admin interface:
    ```bash
    python manage.py createsuperuser

9. **Run the Development Server**:Start the Django development server to run the app locally:
    ```bash
    python manage.py runserver
  The development server will provide a URL (usually http://127.0.0.1:8000/) where you can access your app in a web browser.
  
10. **Access the App**: Open a web browser and navigate to the URL provided by the development server (e.g., http://127.0.0.1:8000/) to access and test the app.




       
