# Network Policies: Securing Pod Communication in Kubernetes

This example demonstrates how to use Kubernetes Network Policies to restrict traffic between pods. Network Policies are essential for securing microservices and controlling which pods can communicate with each other.

---

## Application Overview

The sample application consists of two simple Python Flask services: `app1` and `app2`. Each service responds with its name on the root path (`/`).

**Source:** [`app/app1.py`](./app/app1.py), [`app/app2.py`](./app/app2.py)

---

## Containerization

Each app is containerized using its own Dockerfile:
- Uses `python:3.11-slim` as the base image
- Installs Flask
- Copies the app code
- Exposes port 5000
- Starts the Flask server

**Dockerfiles:** [`app/Dockerfile.app1`](./app/Dockerfile.app1), [`app/Dockerfile.app2`](./app/Dockerfile.app2)

---

## Kubernetes Manifests

- **Deployments:** Deploys both services.
- **Services:** Exposes each app internally.
- **Network Policies:** Restricts traffic so only allowed pods can communicate.

**Manifests:** [`k8s/deployment-app1.yaml`](./k8s/deployment-app1.yaml), [`k8s/deployment-app2.yaml`](./k8s/deployment-app2.yaml), [`k8s/service-app1.yaml`](./k8s/service-app1.yaml), [`k8s/service-app2.yaml`](./k8s/service-app2.yaml), [`k8s/networkpolicy.yaml`](./k8s/networkpolicy.yaml)

---

## Usage

1. Build the Docker images:
   ```bash
   docker build -t networkpolicy-app1:latest -f app/Dockerfile.app1 app/
   docker build -t networkpolicy-app2:latest -f app/Dockerfile.app2 app/
   ```
2. Apply the manifests:
   ```bash
   kubectl apply -f k8s/deployment-app1.yaml
   kubectl apply -f k8s/deployment-app2.yaml
   kubectl apply -f k8s/service-app1.yaml
   kubectl apply -f k8s/service-app2.yaml
   kubectl apply -f k8s/networkpolicy.yaml
   ```

---

