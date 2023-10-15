# Project Procrastinate -  Django App - [Quick Start Guide]

This guide will walk you through the steps to set up and run this Django web application from this GitHub repository.

## Table of Contents

- [Introduction](#introduction)
- [Prerequisites](#prerequisites)
- [Getting Started](#getting-started)
  - [Installation](#installation)
  - [Running the Application](#running-the-application)
- [Contributing](#contributing)
- [Contributors](#contributors)
- [Project Status](#project-status)

## Introduction

This guide will help you get a Django application up and running as quickly as possible.


## Prerequisites

Before you get started, make sure you have the following prerequisites installed on your system:

- **Python**: You can download Python from the [official Python website](https://www.python.org/downloads/).
- **Git**: To clone the repository, you'll need Git. You can download it from [here](https://git-scm.com/downloads).

## Getting Started
Follow these steps to set up and run the Django application:

### Installation

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
### Running the Application

8. **Apply Migrations**: If the app uses a database, apply the necessary database migrations to create tables:
   ```bash
   python manage.py makemigrations
   python manage.py migrate

9. **Create Superuser**:  If the app includes an admin panel, you can create a superuser account to access the admin interface:
    ```bash
    python manage.py createsuperuser

10. **Run the Development Server**:Start the Django development server to run the app locally:
    ```bash
    python manage.py runserver
  The development server will provide a URL (usually http://127.0.0.1:8000/) where you can access your app in a web browser.
  
11. **Access the App**: Open a web browser and navigate to the URL provided by the development server (e.g., http://127.0.0.1:8000/) to access and test the app.



## Contributing

 We welcome your contributions to [Project Procrastinate]! Start by forking the repository, cloning it to your local machine, creating a new branch, making your changes, and committing them. Then, push your changes to your fork on GitHub and create a pull request. Your contributions will be reviewed and, once approved, merged into the main project. Thank you for your help!
## Contributors

A big thank you to the following contributors who have helped improve this project:

- Sonakshi Badlani ([@s0naksh1](https://github.com/s0naksh1))
- Parshva Mody ([@parshvamody15](https://github.com/parshvamody15))

Your contributions are greatly appreciated!

## Project Status

This project is currently under active development, and new features and improvements are being added regularly. While it is functional, there may be occasional updates that could affect usage. We appreciate your understanding and patience as we work to enhance this application. If you encounter any issues or have suggestions, please [open an issue](https://github.com/rakshit-ayachit/project_procrastinate/issues). Your feedback is valuable to us!


       
