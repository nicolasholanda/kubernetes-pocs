# Hello Deployment: Flask App on Kubernetes

This example demonstrates how to deploy a simple Python Flask application to Kubernetes using a Deployment and a Service.

---

## Application Overview

The application is a minimal Flask web server that responds with `Hello from Kubernetes!` on the root path (`/`).

**Source:** [`app/app.py`](./app/app.py)

---

## Containerization

The app is containerized using a simple Dockerfile:
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
  - Uses the image `hello-flask` (build locally)
  - Exposes container port 5000
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
# Build the image (name it hello-flask)
docker build -t hello-flask .
```

### 2. Start Minikube (if not running)
```bash
minikube start
```

### 3. Load the Image into Minikube
If using Minikube, load the image into the cluster:
```bash
minikube image load hello-flask
```

### 4. Deploy to Kubernetes
From the `k8s/` directory:
```bash
cd ../k8s
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
```

### 5. Access the Application
Open the service in your browser:
```bash
minikube service hello-service
```
This will open a browser window to the exposed NodePort. You should see:
```
Hello from Kubernetes!
```

---

## Key Concepts Illustrated
- **Containerization**: Packaging the app with all dependencies
- **Deployment**: Declarative management of pods/replicas
- **Service**: Exposing pods to the network

---

## Clean Up
To remove all resources:
```bash
kubectl delete -f deployment.yaml
kubectl delete -f service.yaml
``` 