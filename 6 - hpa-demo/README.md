# Horizontal Pod Autoscaling (HPA) in Kubernetes

This example demonstrates how to use Horizontal Pod Autoscaler (HPA) to automatically scale your application based on CPU usage in Kubernetes.

---

## Application Overview

The application is a simple Flask web server with an endpoint that generates CPU load for HPA testing.

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
  - Sets CPU resource requests and limits (required for HPA)
  - [deployment.yaml](./k8s/deployment.yaml)

- **Service:**
  - Type: `NodePort` (exposes the app on a port on each node)
  - Forwards port 80 (service) to port 5000 (container)
  - [service.yaml](./k8s/service.yaml)

- **HorizontalPodAutoscaler (HPA):**
  - Scales the deployment between 1 and 5 pods based on average CPU utilization (target: 50%)
  - [hpa.yaml](./k8s/hpa.yaml)

---

## Step-by-Step: Build and Deploy

### 1. Build the Docker Image

From the `app/` directory:
```bash
cd app
# Build the image (name it hpa-demo)
docker build -t hpa-demo .
```

### 2. Start Minikube (if not running)
```bash
minikube start
```

### 3. Load the Image into Minikube
If using Minikube, load the image into the cluster:
```bash
minikube image load hpa-demo
```

### 4. Deploy the Application
From the `k8s/` directory:
```bash
cd ../k8s
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
```

### 5. Deploy the HPA
```bash
kubectl apply -f hpa.yaml
```

### 6. Access the Application
Open the service in your browser:
```bash
minikube service hpa-demo-service
```

---

## Testing HPA Scaling
- The `/cpu` endpoint generates CPU load for 1 second per request.
- To trigger scaling, run this in a separate terminal (replace <NODE-PORT> with the actual NodePort):
  ```bash
  while true; do curl http://<minikube-ip>:<NODE-PORT>/cpu; done
  ```
- Monitor scaling:
  ```bash
  kubectl get hpa
  kubectl get pods
  ```
- The HPA will increase the number of pods if average CPU usage exceeds 50%.

---

## Key Concepts Illustrated
- **Horizontal Pod Autoscaler (HPA):** Automatically scales pods based on resource usage
- **Resource Requests/Limits:** Required for HPA to function
- **CPU-based Scaling:** Example of scaling based on CPU utilization

---

## Clean Up
To remove all resources:
```bash
kubectl delete -f hpa.yaml
kubectl delete -f deployment.yaml
kubectl delete -f service.yaml
``` 