# Persistent Storage: Using Volumes in Kubernetes

This example demonstrates how to use PersistentVolumes (PV) and PersistentVolumeClaims (PVC) to provide persistent storage for your applications in Kubernetes.

---

## Application Overview

The application is a simple Flask web server that writes a timestamp to a file every time it is accessed, and displays the file's contents. The file is stored on a persistent volume, so data survives pod restarts.

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

- **PersistentVolume (PV):**
  - Provides 1Gi of storage using hostPath (for demo purposes)
  - [pv.yaml](./k8s/pv.yaml)

- **PersistentVolumeClaim (PVC):**
  - Requests 1Gi of storage, ReadWriteOnce
  - [pvc.yaml](./k8s/pvc.yaml)

- **Deployment:**
  - Runs 1 replica of the Flask app container
  - Mounts the PVC at `/data` inside the container
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
# Build the image (name it persist-demo)
docker build -t persist-demo .
```

### 2. Start Minikube (if not running)
```bash
minikube start
```

### 3. Load the Image into Minikube
If using Minikube, load the image into the cluster:
```bash
minikube image load persist-demo
```

### 4. Deploy PersistentVolume and PersistentVolumeClaim
From the `k8s/` directory:
```bash
cd ../k8s
kubectl apply -f pv.yaml
kubectl apply -f pvc.yaml
```

### 5. Deploy the Application
```bash
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
```

### 6. Access the Application
Open the service in your browser:
```bash
minikube service persist-demo-service
```
Each refresh will append a new timestamp to the file. Data will persist even if the pod is deleted and recreated.

---

## Key Concepts Illustrated
- **PersistentVolume (PV):** Cluster resource for storage
- **PersistentVolumeClaim (PVC):** Request for storage by a pod
- **Volume Mount:** Mounting storage into a container
- **Persistence:** Data survives pod restarts

---

## Clean Up
To remove all resources:
```bash
kubectl delete -f deployment.yaml
kubectl delete -f service.yaml
kubectl delete -f pvc.yaml
kubectl delete -f pv.yaml
``` 