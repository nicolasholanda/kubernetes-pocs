# ConfigMap and Secret: Managing Configuration in Kubernetes

This example demonstrates how to use Kubernetes ConfigMaps and Secrets to inject configuration and sensitive data into your application pods.

---

## Application Overview

The application is a simple Flask web server that reads a greeting message from a ConfigMap and a secret word from a Secret, then displays both at the root path (`/`).

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

- **ConfigMap:**
  - Provides a `GREETING` environment variable
  - [configmap.yaml](./k8s/configmap.yaml)

- **Secret:**
  - Provides a `SECRET_WORD` environment variable (base64 encoded)
  - [secret.yaml](./k8s/secret.yaml)

- **Deployment:**
  - Runs 1 replica of the Flask app container
  - Injects `GREETING` and `SECRET_WORD` as environment variables from ConfigMap and Secret
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

### 4. Deploy ConfigMap and Secret
From the `k8s/` directory:
```bash
cd ../k8s
kubectl apply -f configmap.yaml
kubectl apply -f secret.yaml
```

### 5. Deploy the Application
```bash
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
```

### 6. Access the Application
Open the service in your browser:
```bash
minikube service hello-config-service
```
You should see something like:
```
Hola from Kubernetes! Secret word: shared_secret
```

---

## Key Concepts Illustrated
- **ConfigMap**: Injecting non-sensitive configuration
- **Secret**: Injecting sensitive data securely
- **Deployment**: Using env variables from ConfigMap/Secret
- **Service**: Exposing pods to the network

---

## Clean Up
To remove all resources:
```bash
kubectl delete -f deployment.yaml
kubectl delete -f service.yaml
kubectl delete -f configmap.yaml
kubectl delete -f secret.yaml
``` 