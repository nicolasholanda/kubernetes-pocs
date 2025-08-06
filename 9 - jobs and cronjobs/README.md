# Jobs and CronJobs: Batch Processing and Scheduling in Kubernetes

This example demonstrates how to run one-off and scheduled tasks in Kubernetes using Jobs and CronJobs. These resources are ideal for batch processing, maintenance routines, and automated backups.

---

## Application Overview

The sample application is a simple Python script that simulates a data processing or backup task.

**Source:** [`app/app.py`](./app/app.py)

---

## Containerization

The app is containerized using a Dockerfile:
- Uses `python:3.11-slim` as the base image
- Copies the app code
- Runs the script on container start

**Dockerfile:** [`app/Dockerfile`](./app/Dockerfile)

---

## Kubernetes Manifests

- **Job:** Runs a single batch task.
- **CronJob:** Schedules recurring jobs (e.g., backups).

**Manifests:** [`k8s/job.yaml`](./k8s/job.yaml), [`k8s/cronjob.yaml`](./k8s/cronjob.yaml)

---

## Usage

1. Build the Docker image:
   ```bash
   docker build -t job-cronjob-demo:latest app/
   ```
2. Apply the manifests:
   ```bash
   kubectl apply -f k8s/job.yaml
   kubectl apply -f k8s/cronjob.yaml
   ```

---

## Note
These examples are for demonstration purposes and can be adapted as needed.
