# Deployment Guide

Since this application is containerized with Docker, it can be deployed to almost any platform that supports containers. Here are a few recommended options:

## Option 1: Render (Easiest & Free Tier)

[Render](https://render.com/) is a cloud platform that makes it easy to deploy web apps.

1.  **Push your code to GitHub** (You have already done this).
2.  **Sign up/Login to Render**.
3.  Click **New +** -> **Web Service**.
4.  Connect your GitHub repository (`titanic-ml-api`).
5.  **Configure**:
    *   **Runtime**: Docker
    *   **Region**: Choose closest to you.
    *   **Free Instance Plan**: Select "Free".
6.  Click **Create Web Service**.

Render will build your Dockerfile and deploy it. You will get a URL (e.g., `https://titanic-ml-api.onrender.com`).

## Option 2: AWS App Runner (Managed Container Service)

AWS App Runner is the easiest way to run containers on AWS without managing servers.

1.  **Push your code to GitHub**.
2.  **Go to AWS Console** -> **App Runner**.
3.  **Create Service**.
4.  **Source**: Source Code Repository.
5.  **Connect GitHub** and select your repo.
6.  NOTE: Select **Configuration in code** (since you have a Dockerfile).
    *   Wait, actually for App Runner with Source Code, it usually builds from a runtime (Python). Use **Container Registry** (ECR) if you want to use the Dockerfile directly, OR use the **Source Code** option and configure the build settings (Runtime: Python 3, Build command: `pip install -r requirements.txt`, Start command: `uvicorn app.main:app --host 0.0.0.0 --port 8080`).
    *   *Better approach for Dockerfile*: Build the image locally and push to **Amazon ECR**, then deploy to App Runner from ECR.

## Option 3: Virtual Machine (AWS EC2 / DigitalOcean / Linode)

This gives you full control.

1.  **Provision a VM** (e.g., Ubuntu).
2.  **SSH into the VM**.
3.  **Install Docker**:
    ```bash
    sudo apt update
    sudo apt install docker.io
    ```
4.  **Clone your repo**:
    ```bash
    git clone https://github.com/Eshwarsai-07/titanic-ml-api.git
    cd titanic-ml-api
    ```
5.  **Build and Run**:
    ```bash
    sudo docker build -t titanic-ml-api .
    sudo docker run -d -p 80:8000 titanic-ml-api
    ```
    (Maps port 80 of the VM to port 8000 of the container).

## Option 4: Kubernetes (Advanced)

If you have a Kubernetes cluster:

1.  **Build and Push** your image to a registry (Docker Hub / ECR).
2.  Create a `deployment.yaml` and `service.yaml`.
3.  Apply with `kubectl apply -f ...`.
