# Project Procrastinate -  Student Resources Manager

Welcome to Project Procrastinate, a comprehensive student resources manager designed to streamline your academic journey. This platform offers a suite of features aimed at enhancing studying efficiency and resource accessibility.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Getting Started](#getting-started)
  - [Installation](#installation)
  - [Running the Application](#running-the-application)
- [Screenshots](#screenshots)
- [Contributing](#contributing)
- [Contributors and Contact](#contributors-and-contact)
- [Project Status](#project-status)
- [License](#license)

## Introduction

Project Procrastinate is a dynamic tool that integrates various functionalities to support students in managing their educational materials, accessing courses, generating course recommendations, and interacting with an AI chatbot for academic assistance.

## Features

1. **Profile Page:** Users have personalized profile pages displaying their details and preferences for a tailored experience.

2. **Homepage Course Management:** The homepage displays a customizable list of relevant courses, allowing users to add or delete courses according to their preferences. Each course includes comprehensive details such as professor names, semester information, notes, past year papers, and quiz details.

3. **Coursera Course Recommendor:** Hosted on Streamlit, this feature recommends courses based on user preferences, fostering personalized learning experiences.

4. **AI Chatbot Assistance:** A smart AI chatbot is available to provide real-time support for academic queries and study materials.

5. **Upload Portal with Authentication:** Seniors can securely upload materials, reviewed by website collaborators to ensure authenticity and relevance.

6. **Authentication System:** A secure login/logout window ensures user privacy, with a seamless signup process for new users.


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
    python manage.py runserver localhost:8080
  The development server will provide a URL (usually http://127.0.0.1:8080/) where you can access your app in a web browser.
  
11. **Access the App**: Open a web browser and navigate to the URL provided by the development server (e.g., http://127.0.0.1:8080/) to access and test the app.

## Screenshots
![signup](https://github.com/rakshit-ayachit/project_procrastinate/assets/129822642/5d36ce84-5af0-4b3e-bdad-4c26c58e4d2e)
![homepage](https://github.com/rakshit-ayachit/project_procrastinate/assets/129822642/6f6d6200-d2ad-425a-9a4c-a15d9f77d204)
![profile](https://github.com/rakshit-ayachit/project_procrastinate/assets/129822642/37be3d1c-17d6-4825-87d1-500a90b941f3)
![course-recommendor](https://github.com/rakshit-ayachit/project_procrastinate/assets/129822642/77383d18-a404-432c-91fd-6f2320ae03cb)
![upload](https://github.com/rakshit-ayachit/project_procrastinate/assets/129822642/1ecfc456-07c7-4aec-acb7-17cb656eee76)


## Contributing

 We welcome your contributions to [Project Procrastinate](https://github.com/rakshit-ayachit/project_procrastinate)! Start by forking the repository, cloning it to your local machine, creating a new branch, making your changes, and committing them. Then, push your changes to your fork on GitHub and create a pull request. Your contributions will be reviewed and, once approved, merged into the main project. Thank you for your help!
## Contributors and Contact

A big thank you to the following contributors who have helped improve this project:

- Sonakshi Badlani ([@s0naksh1](https://github.com/s0naksh1)) - [sonakshibadlani@gmail.com](mailto:sonakshibadlani@gmail.com)
- Parshva Mody ([@parshvamody15](https://github.com/parshvamody15)) - [parshvapmody@gmail.com](mailto:parshvapmody@gmail.com)

Your contributions are greatly appreciated!

Feel free to contact me ([Rakshit Ayachit](mailto:rakshit@ayachit@gmail.com)) or any of the contributors for further information or support regarding this project.


## Project Status

This project is currently under active development, and new features and improvements are being added regularly. While it is functional, there may be occasional updates that could affect usage. We appreciate your understanding and patience as we work to enhance this application. If you encounter any issues or have suggestions, please [open an issue](https://github.com/rakshit-ayachit/project_procrastinate/issues). Your feedback is valuable to us!

## License

This project is licensed under the [MIT License](LICENSE).

