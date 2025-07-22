#!/bin/bash
set -e

echo "Starting minikube..."
minikube start --driver=docker

echo "Enabling dashboard..."
minikube dashboard &
