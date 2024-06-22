# My Flask App

This is a Flask-based web application that uses MySQL as a database. The project is containerized using Docker for easy deployment and scalability.

## Description

This application is designed to demonstrate the use of Flask for creating web applications with a MySQL database backend. The application is containerized using Docker, making it easy to deploy and run in various environments.

## Features

- **Flask Web Framework**: A lightweight WSGI web application framework.
- **MySQL Database**: Used for persistent data storage.
- **REST API**: Implements a simple API for data interaction.
- **Dockerized**: Containerized application for easy deployment.

## Project Structure

├── Dockerfile
├── README.md
├── app.py
├── requirements.txt
├── static
│ └── ... (static files like CSS, JS, images)
├── templates
│ └── ... (HTML templates)

makefile

## Prerequisites

- Docker: Ensure Docker is installed and running on your system.
- Docker Hub Account: You need an account on Docker Hub to push the Docker image.

## Setup

### 1. Create `requirements.txt`

Create a `requirements.txt` file with the following content:

```plaintext
blinker==1.8.2
certifi==2024.6.2
charset-normalizer==3.3.2
click==8.1.7
colorama==0.4.6
Flask==3.0.3
idna==3.7
itsdangerous==2.2.0
Jinja2==3.1.4
MarkupSafe==2.1.5
mysql-connector-python==8.4.0
requests==2.32.3
urllib3==2.2.2
Werkzeug==3.0.3
gunicorn==20.1.0


2. Create Dockerfile
Create a Dockerfile with the following content:
# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Run Gunicorn server when the container launches
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "app:app"]
Building and Running the Docker Container
1. Build the Docker image
docker build -t my-flask-app .
2. Run the Docker container

docker run -p 5000:5000 my-flask-app
The application will be accessible at http://localhost:5000.

Pushing the Docker Image to Docker Hub
1. Log in to Docker Hub
docker login
2. Tag the Docker image
docker tag my-flask-app your-username/my-flask-app:latest
3. Push the Docker image
docker push your-username/my-flask-app:latest
Pulling and Running the Docker Image from Docker Hub
1. Pull the Docker image
docker pull your-username/my-flask-app:latest
2. Run the Docker container
docker run -p 5000:5000 your-username/my-flask-app:latest
Usage
Once the application is running, you can interact with it through your web browser or API client (like Postman) at http://localhost:5000. The application provides a web interface for interacting with the MySQL database and a simple API for data operations.

Development
To set up a development environment, follow these steps:

Clone the repository:


git clone https://github.com/your-username/my-flask-app.git
cd my-flask-app
Create and activate a virtual environment:
python3 -m venv venv
source venv/bin/activate
Install dependencies:


pip install -r requirements.txt
Run the application:

flask run
Contribution
If you wish to contribute to the project, follow these steps:

Fork the repository on GitHub.
Clone your fork locally:
git clone https://github.com/your-username/my-flask-app.git
cd my-flask-app
Create a new branch for your feature or bug fix:

git checkout -b feature-or-bugfix-name
Make your changes and commit them:

git commit -m "Description of your changes"
Push to your fork:
git push origin feature-or-bugfix-name
Create a pull request on GitHub.
License
This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgments
Flask: Flask
Docker: Docker
