# Ingress Controller: Path-Based Routing in Kubernetes

This example demonstrates how to use an Ingress controller to route traffic to multiple services based on URL paths in Kubernetes.

---

## Application Overview

The application consists of two simple Flask web servers that will be accessed through different URL paths via the Ingress controller.

**Source:** 
- [`app/app1.py`](./app/app1.py) - Frontend service
- [`app/app2.py`](./app/app2.py) - Backend service

---

## Containerization

Both apps are containerized using Dockerfiles:
- Uses `python:3.11-slim` as the base image
- Installs Flask
- Copies the respective app code
- Exposes port 5000
- Starts the Flask server

**Dockerfiles:** 
- [`app/Dockerfile.app1`](./app/Dockerfile.app1)
- [`app/Dockerfile.app2`](./app/Dockerfile.app2)

---

## Kubernetes Manifests

All Kubernetes resources are defined in the [`k8s/`](./k8s/) directory:

- **Deployments:**
  - `app1-deployment` - Runs 1 replica of the frontend app
  - `app2-deployment` - Runs 1 replica of the backend app
  - [deployment-app1.yaml](./k8s/deployment-app1.yaml)
  - [deployment-app2.yaml](./k8s/deployment-app2.yaml)

- **Services:**
  - `app1-service` - ClusterIP service for frontend app
  - `app2-service` - ClusterIP service for backend app
  - [service-app1.yaml](./k8s/service-app1.yaml)
  - [service-app2.yaml](./k8s/service-app2.yaml)

- **Ingress:**
  - Routes `/app1` traffic to app1-service
  - Routes `/app2` traffic to app2-service
  - [ingress.yaml](./k8s/ingress.yaml)

---

## Step-by-Step: Build and Deploy

### 1. Enable Ingress Addon in Minikube
```bash
minikube addons enable ingress
```

### 2. Build the Docker Images

From the `app/` directory:
```bash
cd app
# Build both images
docker build -f Dockerfile.app1 -t app1:latest .
docker build -f Dockerfile.app2 -t app2:latest .
```

### 3. Start Minikube (if not running)
```bash
minikube start
```

### 4. Load the Images into Minikube
If using Minikube, load the images into the cluster:
```bash
minikube image load app1:latest
minikube image load app2:latest
```

### 5. Deploy the Applications
From the `k8s/` directory:
```bash
cd ../k8s
kubectl apply -f deployment-app1.yaml
kubectl apply -f deployment-app2.yaml
kubectl apply -f service-app1.yaml
kubectl apply -f service-app2.yaml
```

### 6. Deploy the Ingress
```bash
kubectl apply -f ingress.yaml
```

### 7. Access the Applications
Get the Minikube IP:
```bash
minikube ip
```

Then access the apps via:
- Frontend: `http://<minikube-ip>/app1`
- Backend: `http://<minikube-ip>/app2`

---

## Testing Ingress Routing
- Visit `http://<minikube-ip>/app1` - Should show "App 1 - Frontend Service"
- Visit `http://<minikube-ip>/app2` - Should show "App 2 - Backend Service"
- Visit `http://<minikube-ip>/app1/api` - Should show "App 1 API Endpoint"
- Visit `http://<minikube-ip>/app2/data` - Should show "App 2 Data Endpoint"

---

## Key Concepts Illustrated
- **Ingress Controller:** Routes external traffic to internal services
- **Path-Based Routing:** Different URL paths route to different services
- **ClusterIP Services:** Internal services that Ingress can route to
- **Single Entry Point:** One external IP serves multiple applications

---

## Clean Up
To remove all resources:
```bash
kubectl delete -f ingress.yaml
kubectl delete -f service-app1.yaml
kubectl delete -f service-app2.yaml
kubectl delete -f deployment-app1.yaml
kubectl delete -f deployment-app2.yaml
``` 