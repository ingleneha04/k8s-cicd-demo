# Kubernetes CI/CD Demo Application

A beginner-friendly DevOps project demonstrating how to containerize a Flask application using Docker and deploy it to Kubernetes using Minikube.

## Project Overview

This project demonstrates:
- Building a Flask web application with a health endpoint
- Creating a Docker image
- Deploying the application to Kubernetes
- Running two application replicas
- Exposing the application using a Kubernetes NodePort Service
- Configuring readiness and liveness probes

## Tech Stack

- Python and Flask
- Docker
- Kubernetes
- Minikube
- kubectl
- Git and GitHub

## Project Structure

```text
k8s-cicd-project/
├── app/
│   └── app.py
├── Kubernetes/
│   ├── deployment.yaml
│   └── service.yaml
├── Dockerfile
├── requirements.txt
├── .gitignore
└── README.md
```

## Run Locally with Docker

Build the image:

```bash
docker build -t k8s-cicd-demo:v1 .
```

Run the container:

```bash
docker run --rm -p 5000:5000 k8s-cicd-demo:v1
```

Open:
- Application: http://localhost:5000
- Health check: http://localhost:5000/health

## Deploy to Kubernetes

Start Minikube:

```bash
minikube start --profile=devops
```

Build the image in Minikube's Docker environment using PowerShell:

```powershell
minikube -p devops docker-env --shell powershell | Invoke-Expression
docker build -t k8s-cicd-demo:v1 .
```

Deploy the application:

```bash
kubectl apply -f Kubernetes/deployment.yaml
kubectl apply -f Kubernetes/service.yaml
```

Verify the deployment:

```bash
kubectl get deployments
kubectl get pods
kubectl get services
```

Access the application:

```bash
minikube service k8s-cicd-demo-service --profile=devops
```

Keep the terminal open while using the Minikube service tunnel.

## Health Endpoint

The `/health` endpoint returns HTTP 200 when the application is healthy. Kubernetes uses this endpoint for readiness and liveness probes.

## Current Features

- Containerized Flask application
- Kubernetes Deployment with two replicas
- NodePort Service
- Readiness and liveness probes

## Planned Improvements

- GitHub Actions CI pipeline
- Automated testing
- Container image publishing
- CI/CD deployment workflow
- Prometheus and Grafana monitoring

## Author

DevOps Portfolio Project
