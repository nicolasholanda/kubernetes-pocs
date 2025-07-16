# Kubernetes

Kubernetes (K8s) is an open-source system for automating the deployment, scaling, and management of containerized applications. It provides a platform for running containers across a cluster of machines (physical or virtual) in a consistent and declarative way.

## Kubernetes vs Docker Compose

While Docker allows packaging and running applications in containers, it lacks built-in features for:
* **Managing many containers across multiple hosts**
* **Self-healing applications** (e.g., restart if a container crashes)
* **Auto-scaling** based on usage
* **Rolling updates** without downtime
* **Service discovery** and networking
* **Managing secrets, configuration, and persistent storage**

Kubernetes addresses these concerns by acting as an orchestrator for containers.

## Key Concepts
* **Node**: A physical or virtual machine that runs container workloads.
* **Pod**: The smallest deployable unit in Kubernetes. A pod wraps one or more containers and shares their resources (network, storage). Pods are ephemeral and typically managed by higher-level objects.
* **Deployment**: Describes how many replicas of a pod should run, and how they should be updated.
* **Service**: An abstraction that exposes a set of pods as a network service, enabling communication inside and outside the cluster.
* **Namespace**: A way to divide cluster resources logically between users or applications.
* **ConfigMap and Secret**: Used to manage configuration data and sensitive data (like API keys), respectively.
* **Volume**: A way to persist and share data across container restarts and pod re-creations.

## CLI Tools for Working with Kubernetes
* **kubectl**: The official command-line tool to interact with Kubernetes clusters. It can be used to apply configurations, inspect resources, and perform administrative tasks. 
  
  Example commands:
  * `kubectl apply -f deployment.yaml` — applies a configuration file
  * `kubectl get pods` — lists current running pods
  * `kubectl describe service my-service` — shows details of a service

* **minikube**: A tool that runs a single-node Kubernetes cluster locally. It is useful for learning and local development.

  Common commands:
  * **minikube start** — starts the local cluster
  * **minikube dashboard** — launches a GUI dashboard in the browser
  * **minikube service my-service** — opens a URL to access a Kubernetes service

## Kubernetes Cluster Overview
A Kubernetes cluster is the foundation of a K8s environment. It consists of two types of components:

### 1. Control Plane (Master Components)

Responsible for maintaining the desired state of the cluster.

* **kube-apiserver**: Frontend to the cluster. All commands and interactions go through it.
* **etcd**: Key-value store for cluster data (configuration, state).
* **kube-scheduler**: Assigns newly created workloads (pods) to nodes.
* **kube-controller-manager**: Ensures cluster state matches the desired configuration.
* **cloud-controller-manager**: Handles cloud provider-specific logic (e.g., AWS, GCP).

### 2. Worker Nodes

Machines that actually run application workloads.

* **kubelet**: Agent running on each node; it ensures containers are running as instructed.
* **kube-proxy**: Manages networking and load balancing inside the cluster.
* **container runtime**: Software that runs containers (e.g., Docker, containerd, CRI-O).

![Kubernetes Cluster](./module_01_clusters.svg)