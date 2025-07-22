# Health Checks: Liveness and Readiness Probes in Kubernetes

This example demonstrates how to use liveness and readiness probes to monitor and manage application health in Kubernetes.

---

## Application Overview

The application is a simple Flask web server with endpoints for health and readiness checks. You can simulate readiness/unreadiness by creating or deleting a file inside the container.

**Source:** [`app/app.py`](./app/app.py)

---

## Containerization

The app is containerized using a Dockerfile:
- Uses `python:3.11-slim` as the base image
- Installs Flask
- Copies the app code
- Exposes port 5000
- Starts the Flask server

**Dockerfile:** [`app/Dockerfile`](./app/Dockerfile)

---

## Kubernetes Manifests

All Kubernetes resources are defined in the [`k8s/`](./k8s/) directory:

- **Deployment:**
  - Runs 1 replica of the Flask app container
  - Adds a liveness probe (`/healthz`) and a readiness probe (`/ready`)
  - [deployment.yaml](./k8s/deployment.yaml)

- **Service:**
  - Type: `NodePort` (exposes the app on a port on each node)
  - Forwards port 80 (service) to port 5000 (container)
  - [service.yaml](./k8s/service.yaml)

---

## Step-by-Step: Build and Deploy

### 1. Build the Docker Image

From the `app/` directory:
```bash
cd app
# Build the image (name it health-checks-demo)
docker build -t health-checks-demo .
```

### 2. Start Minikube (if not running)
```bash
minikube start
```

### 3. Load the Image into Minikube
If using Minikube, load the image into the cluster:
```bash
minikube image load health-checks-demo
```

### 4. Deploy the Application
From the `k8s/` directory:
```bash
cd ../k8s
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
```

### 5. Access the Application
Open the service in your browser:
```bash
minikube service health-checks-demo-service
```

---

## Testing Liveness and Readiness
- The liveness probe (`/healthz`) always returns 200 OK. If it fails, Kubernetes will restart the container.
- The readiness probe (`/ready`) returns 200 OK only if the file `/tmp/ready` exists. Otherwise, it returns 503.
- Use `/make-ready` and `/make-unready` endpoints to simulate readiness:
  - `curl http://<service-url>/make-ready` — pod becomes ready
  - `curl http://<service-url>/make-unready` — pod becomes unready

---

## Key Concepts Illustrated
- **Liveness Probe:** Detects if the app is running. Restarts the container if it fails.
- **Readiness Probe:** Detects if the app is ready to serve traffic. Removes pod from service endpoints if it fails.

---

## Clean Up
To remove all resources:
```bash
kubectl delete -f deployment.yaml
kubectl delete -f service.yaml
``` 