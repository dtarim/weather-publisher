# 🌍 Weather Publisher & Server

This project consists of two components: a **Publisher** and a **Server**, working together to collect and display real-time weather information for 60 cities across 6 continents.

---

## 🧩 Project Overview

- **Publisher**  
  - Reads a list of cities from a JSON structure embedded in its code  
  - Fetches current weather data for each city using the free API at `https://wttr.in`  
  - Sends the collected weather data to the server via HTTP POST request  

- **Server**  
  - Receives weather data from the publisher  
  - Stores the data in memory during runtime  
  - Displays all cities and their current temperatures on a simple web page  

---

## 📁 Project Structure

The project consists of two main folders: `publisher` and `server`.

- **publisher/**  
  Contains the script `publisher.py` that fetches weather data and sends it to the server.  
  It includes a hardcoded list of cities grouped by continent inside the script (no external JSON file needed).  
  Requires Python dependencies: `requests`.

- **server/**  
  Contains the Flask server script `server.py` which receives data and serves a web page showing the weather.  
  Uses Flask and Jinja2 template engine for HTML rendering.  
  Contains an embedded HTML template within the script or in a templates folder.

---

🔧 Technologies Used
Python 3.11+ for both components

Flask for the server to provide API and web interface

Requests library for HTTP requests in the publisher

wttr.in as a free weather API service

 ---

🛠️ Automation & Containerization

**GitHub Actions CI is configured to:**

Run on push and pull request events targeting the master branch.

Checkout the code.

Setup Python 3.11 environment.

Install dependencies from requirements.txt (if available).

Run lint checks with flake8 for code quality.

**Docker:**

Docker images are built for consistent environment and deployment.

This allows easier distribution and future scaling.

Containerization also prepares the project for cloud or Kubernetes deployment.


🎯 Purpose and Learning Goals

Understand HTTP client-server communication in Python

Learn to build REST APIs and dynamic web pages with Flask

Practice consuming third-party APIs (wttr.in)

Prepare for containerization (Docker) and automated CI/CD workflows

Gain hands-on experience with modular Python projects

🔮 Future Plans
Containerize the publisher and server with Docker

Publish images to Docker Hub or private registries

Create automated tests and deployment pipelines with GitHub Actions

Deploy on Kubernetes for scalability and fault tolerance

Add persistent storage with a database

Implement authentication and enhanced UI

👩‍💻 About the Author
This project was created by Didem TARIM as part of learning Python web development, API integration, and DevOps practices.

