# RBAC (Role-Based Access Control) in Kubernetes

This example demonstrates how to use RBAC to control access to Kubernetes resources through roles, role bindings, and service accounts.

---

## Application Overview

The application is a simple Flask web server that serves different endpoints to demonstrate access control. Different service accounts will have different levels of access to Kubernetes resources.

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

- **Namespace:**
  - `rbac-demo` - Isolates all RBAC demo resources
  - [namespace.yaml](./k8s/namespace.yaml)

- **Service Accounts:**
  - `admin-user` - Has full permissions
  - `readonly-user` - Has read-only permissions
  - [serviceaccount-admin.yaml](./k8s/serviceaccount-admin.yaml)
  - [serviceaccount-readonly.yaml](./k8s/serviceaccount-readonly.yaml)

- **Roles:**
  - `admin-role` - ClusterRole with full permissions
  - `readonly-role` - Role with read-only permissions in namespace
  - [role-admin.yaml](./k8s/role-admin.yaml)
  - [role-readonly.yaml](./k8s/role-readonly.yaml)

- **Role Bindings:**
  - `admin-binding` - Binds admin role to admin user
  - `readonly-binding` - Binds readonly role to readonly user
  - [rolebinding-admin.yaml](./k8s/rolebinding-admin.yaml)
  - [rolebinding-readonly.yaml](./k8s/rolebinding-readonly.yaml)

- **Deployment:**
  - Runs 1 replica of the Flask app container
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
# Build the image (name it rbac-demo)
docker build -t rbac-demo .
```

### 2. Start Minikube (if not running)
```bash
minikube start
```

### 3. Load the Image into Minikube
If using Minikube, load the image into the cluster:
```bash
minikube image load rbac-demo
```

### 4. Create Namespace and RBAC Resources
From the `k8s/` directory:
```bash
cd ../k8s
kubectl apply -f namespace.yaml
kubectl apply -f serviceaccount-admin.yaml
kubectl apply -f serviceaccount-readonly.yaml
kubectl apply -f role-admin.yaml
kubectl apply -f role-readonly.yaml
kubectl apply -f rolebinding-admin.yaml
kubectl apply -f rolebinding-readonly.yaml
```

### 5. Deploy the Application
```bash
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
```

### 6. Access the Application
Open the service in your browser:
```bash
minikube service rbac-demo-service -n rbac-demo
```

---

## Testing RBAC Permissions

### Test Admin User Permissions
```bash
# Switch to admin user context
kubectl config set-context --current --user=admin-user

# Test admin permissions
kubectl get pods -n rbac-demo
kubectl get services -n rbac-demo
kubectl delete pod <pod-name> -n rbac-demo  # Should work
```

### Test Read-Only User Permissions
```bash
# Switch to readonly user context
kubectl config set-context --current --user=readonly-user

# Test readonly permissions
kubectl get pods -n rbac-demo  # Should work
kubectl get services -n rbac-demo  # Should work
kubectl delete pod <pod-name> -n rbac-demo  # Should fail
```

### Check Service Account Tokens
```bash
# Get admin user token
kubectl get secret -n rbac-demo $(kubectl get serviceaccount admin-user -n rbac-demo -o jsonpath='{.secrets[0].name}') -o jsonpath='{.data.token}' | base64 -d

# Get readonly user token
kubectl get secret -n rbac-demo $(kubectl get serviceaccount readonly-user -n rbac-demo -o jsonpath='{.secrets[0].name}') -o jsonpath='{.data.token}' | base64 -d
```

---

## Key Concepts Illustrated
- **Service Accounts:** Identities for pods and users
- **Roles:** Define permissions on resources
- **Role Bindings:** Assign roles to users/groups/service accounts
- **Namespace Isolation:** Resources and permissions scoped to namespaces
- **ClusterRole vs Role:** Cluster-wide vs namespace-scoped permissions

---

## Clean Up
To remove all resources:
```bash
kubectl delete -f service.yaml
kubectl delete -f deployment.yaml
kubectl delete -f rolebinding-readonly.yaml
kubectl delete -f rolebinding-admin.yaml
kubectl delete -f role-readonly.yaml
kubectl delete -f role-admin.yaml
kubectl delete -f serviceaccount-readonly.yaml
kubectl delete -f serviceaccount-admin.yaml
kubectl delete -f namespace.yaml
``` 