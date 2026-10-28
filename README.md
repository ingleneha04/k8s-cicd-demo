	# Kubernetes CI/CD Demo Project

A DevOps project demonstrating automated CI/CD, containerization, Kubernetes deployment, Prometheus monitoring, and Grafana alerting.

## Project Overview

This project deploys a Python Flask application to Kubernetes using Docker and GitHub Actions. Prometheus collects application metrics, while Grafana visualizes metrics and monitors HTTP 500 errors through alert rules.

## Architecture

```text
Developer
    |
    v
GitHub Repository
    |
    v
GitHub Actions CI/CD
    |
    +--> Install Python dependencies
    +--> Run Pytest tests
    +--> Check Python syntax
    +--> Build Docker image
    +--> Push image to Docker Hub
    |
    v
Self-hosted GitHub Actions Runner
    |
    v
Minikube / Kubernetes
    |
    +--> Flask Application (2 replicas)
    +--> Kubernetes Service
    |
    v
Prometheus
    |
    v
Grafana Dashboard and Alerting
```

## Technologies Used

* Python and Flask
* Docker and Docker Hub
* Kubernetes and Minikube
* GitHub Actions
* Prometheus
* Grafana
* Pytest
* PowerShell

## Application Endpoints

| Endpoint      | Purpose                                         |
| ------------- | ----------------------------------------------- |
| `/`           | Application information                         |
| `/health`     | Health check                                    |
| `/metrics`    | Prometheus metrics                              |
| `/test-error` | Generate an HTTP 500 response for alert testing |

## CI/CD Pipeline

The GitHub Actions pipeline is configured in `.github/workflows/ci.yml`.

On pushes to `main`, the workflow:

1. Checks out the repository.
2. Sets up Python 3.12.
3. Installs dependencies.
4. Runs automated tests.
5. Checks Python syntax.
6. Builds and pushes a Docker image to Docker Hub.

The deployment workflow is configured in `.github/workflows/deploy.yml` and uses a self-hosted runner to deploy the selected image to local Minikube.

## Kubernetes Deployment

The application runs with two replicas in Kubernetes.

Useful commands:

```powershell
kubectl get deployments
kubectl get pods -l app=k8s-cicd-demo
kubectl get svc k8s-cicd-demo-service
kubectl rollout status deployment/k8s-cicd-demo
```

## Monitoring with Prometheus

The Flask application exposes metrics at `/metrics`, including:

* `app_http_requests_total`
* `app_http_request_duration_seconds`

A ServiceMonitor discovers the application metrics endpoint.

Example PromQL query:

```promql
sum(rate(app_http_requests_total{http_status=~"5.."}[5m])) or vector(0)
```

## Grafana Alerting

The Grafana alert rule `K8s-CICD-App-HTTP-Errors` monitors HTTP 5xx errors.

Example alert test:

```powershell
Invoke-WebRequest http://localhost:5025/test-error -UseBasicParsing -SkipHttpErrorCheck
```

Expected HTTP status: `500`.

The alert was tested and reached the `Firing` state.

## Verification

The following checks were completed during project testing:

* GitHub Actions workflows completed successfully.
* Kubernetes application replicas reached `Running`.
* The `/metrics` endpoint returned HTTP 200.
* Prometheus discovered the application metrics.
* The Grafana HTTP error alert reached `Firing` during testing.

## Repository Structure

```text
k8s-cicd-project/
├── .github/
│   └── workflows/
│       ├── ci.yml
│       └── deploy.yml
├── app/
│   └── app.py
├── Kubernetes/
│   ├── service.yaml
│   └── servicemonitor.yaml
├── tests/
├── Dockerfile
├── requirements.txt
├── deploy-local.ps1
└── README.md
```

## Future Improvements

* Add Kubernetes resource requests and limits.
* Add automated rollback on deployment failure.
* Improve dashboards for request rate, latency, and error rate.
* Add additional automated integration tests.

## Author

DevOps / Cloud Engineering Project

Built to practice CI/CD automation, container orchestration, monitoring, and alerting.
