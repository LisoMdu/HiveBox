# HiveBox

A scalable RESTful API project built around [openSenseMap](https://opensensemap.org/) data, customized to help beekeepers monitor environmental conditions. This project is being built incrementally as part of the [DevOps Roadmap HiveBox project](https://devopsroadmap.io/projects/hivebox/).

## Project Status

**Current version:** `v0.1.0` (Phase 4)

The application is a REST API built with FastAPI, exposing endpoints for version information, real-time temperature data sourced from openSenseMap senseBoxes, and Prometheus metrics. It is deployed on a local Kubernetes cluster using KIND with Ingress-Nginx.

## Prerequisites

To build and run this project locally, you'll need:

- [Git](https://git-scm.com/)
- [Docker](https://www.docker.com/)
- [KIND](https://kind.sigs.k8s.io/)
- [kubectl](https://kubernetes.io/docs/tasks/tools/)
- [Helm](https://helm.sh/)
- (Optional, for running without Docker/Kubernetes) Python 3.12

## Project Structure

```
HiveBox/
├── app.py                        # Main application entry point
├── Dockerfile                    # Container definition
├── requirements.txt              # Python dependencies
├── .dockerignore                 
├── .gitignore                    
├── k8s/                          # Kubernetes manifests
│   ├── kind-config.yaml          # KIND cluster configuration
│   ├── deployment.yaml           # HiveBox deployment manifest
│   ├── service.yaml              # HiveBox service manifest
│   └── ingress.yaml              # Ingress routing rules
└── .github/
    └── workflows/
        ├── ci.yml                # CI pipeline
        └── cd.yml                # CD pipeline
```

## API Endpoints

### `GET /version`
Returns the current version of the deployed application.

- **Parameters:** None
- **Example response:**
  ```json
  "0.1.0"
  ```

### `GET /temperature`
Returns the current average temperature based on live senseBox data from openSenseMap. Only uses sensor readings no older than 1 hour.

- **Parameters:** None
- **Example response:**
  ```json
  {
    "average_temperature": 21.4,
    "status": "Good"
  }
  ```
- **Status values:**
  - `Too Cold` — average temperature below 10°C
  - `Good` — average temperature between 10°C and 37°C
  - `Too Hot` — average temperature above 37°C

### `GET /metrics`
Returns default Prometheus metrics about the application.

- **Parameters:** None
- **Response format:** Prometheus text exposition format (not JSON)

## Running Locally (without Docker)

1. Clone this repository and navigate into the project directory.
2. Create and activate a Python virtual environment.
3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
4. Start the application:
   ```
   uvicorn app:app --reload
   ```
5. Open your browser and navigate to `http://localhost:8000/docs` to explore and test the API interactively.

## Building and Running with Docker

1. Build the Docker image:
   ```
   docker build -t hivebox:latest .
   ```
2. Run the container:
   ```
   docker run -p 8000:8000 hivebox:latest
   ```
3. The API will be available at `http://localhost:8000`.

## Kubernetes Deployment (KIND)

### 1. Create the KIND cluster
```
kind create cluster --config k8s/kind-config.yaml
```

### 2. Install Ingress-Nginx
```
kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/main/deploy/static/provider/kind/deploy.yaml
```

Wait for Ingress-Nginx to be ready:
```
kubectl wait --namespace ingress-nginx \
  --for=condition=ready pod \
  --selector=app.kubernetes.io/component=controller \
  --timeout=90s
```

### 3. Load the Docker image into KIND
```
docker build -t hivebox:latest .
kind load docker-image hivebox:latest
```

### 4. Apply the Kubernetes manifests
```
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml
kubectl apply -f k8s/ingress.yaml
```

### 5. Verify everything is running
```
kubectl get pods
kubectl get service
kubectl get ingress
```

Wait until the pod shows `Running` status, then the API will be available at `http://localhost`.

## Manual Testing

Once the application is running (either locally or via Kubernetes), you can test the endpoints in any of the following ways:

**Interactive docs (recommended):**
- Local: `http://localhost:8000/docs`
- Kubernetes: `http://localhost/docs`

**Browser or curl:**
```
curl http://localhost/version
curl http://localhost/temperature
curl http://localhost/metrics
```

## Continuous Integration

This project uses GitHub Actions for CI. The pipeline runs automatically on every push and pull request and performs the following steps:

1. Lint Python code with `pylint`
2. Lint the Dockerfile with `hadolint`
3. Scan Kubernetes manifests for misconfigurations with `Terrascan`
4. Build the Docker image

Security posture is also monitored via the [OpenSSF Scorecard GitHub Action](https://securityscorecards.dev/#using-the-github-action).

## Continuous Delivery

A separate CD pipeline triggers automatically when a version tag (e.g. `v0.1.0`) is pushed. It builds the Docker image and publishes it to the GitHub Container Registry (GHCR):

```
ghcr.io/your-github-username/hivebox:0.1.0
```

To trigger a release:
```
git tag v0.1.0
git push origin v0.1.0
```

The published image can be pulled directly from GHCR:
```
docker pull ghcr.io/your-github-username/hivebox:0.1.0
```

## Versioning

This project follows [Semantic Versioning](https://semver.org/). Each release is tagged in this repository and published to GHCR automatically via the CD pipeline.

## Roadmap

This project is developed incrementally, phase by phase, following the [HiveBox project roadmap](https://devopsroadmap.io/projects/hivebox/). Each phase is implemented in its own pull request against `main`.

- [x] Phase 1 — Project setup and planning
- [x] Phase 2 — Initial versioned app (`v0.0.1`), Dockerfile, and local testing workflow
- [x] Phase 3 — REST API endpoints (`/version`, `/temperature`), Docker best practices, CI pipeline
- [x] Phase 4 — Kubernetes deployment with KIND and Ingress-Nginx, `/metrics` endpoint, temperature status field, Terrascan, CD pipeline with GHCR
- [ ] Phase 5 — Caching with Valkey, storage with MinIO, Helm charts, observability