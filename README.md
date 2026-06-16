# HiveBox

A scalable RESTful API project built around [openSenseMap](https://opensensemap.org/) data, customized to help beekeepers monitor environmental conditions. This project is being built incrementally as part of the [DevOps Roadmap HiveBox project](https://devopsroadmap.io/projects/hivebox/).

## Project Status

**Current version:** `v0.1.0` (Phase 3)

The application is a REST API built with FastAPI, exposing endpoints for version information and real-time temperature data sourced from openSenseMap senseBoxes.

## Prerequisites

To build and run this project, you'll need:

- [Git](https://git-scm.com/)
- [Docker](https://www.docker.com/)
- (Optional, for running without Docker) Python 3.12

## Project Structure

- `app.py` — main application entry point; contains the FastAPI app and all endpoint definitions
- `requirements.txt` — Python dependencies
- `Dockerfile` — defines how the app is containerized following Docker best practices
- `.dockerignore` / `.gitignore` — exclude unnecessary files from the image and repository
- `.github/workflows/ci.yml` — GitHub Actions CI pipeline

## API Endpoints

### `GET /version`
Returns the current version of the deployed application.

- **Parameters:** None
- **Example response:**
  ```json
  "0.1.0"
  ```

### `GET /temperature`
Returns the current average temperature based on live senseBox data from openSenseMap.

- **Parameters:** None
- **Requirements:** Only uses sensor readings no older than 1 hour.
- **Example response:**
  ```json
  { "average_temperature": 21.4 }
  ```

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
   docker build -t hivebox:0.1.0 .
   ```
2. Run the container:
   ```
   docker run -p 8000:8000 hivebox:0.1.0
   ```
3. The API will be available at `http://localhost:8000`.

## Manual Testing

Once the container is running, you can test the endpoints in any of the following ways:

**Interactive docs (recommended):**
Navigate to `http://localhost:8000/docs` in your browser. FastAPI's built-in Swagger UI lets you execute requests directly from the browser.

**Browser:**
For GET endpoints, paste the URL directly into your browser's address bar:
- `http://localhost:8000/version`
- `http://localhost:8000/temperature`

**curl:**
```
curl http://localhost:8000/version
curl http://localhost:8000/temperature
```

## Continuous Integration

This project uses GitHub Actions for CI. The pipeline runs automatically on every push and pull request against `main` and performs the following steps:

1. Lint Python code with `pylint`
2. Lint the Dockerfile with `hadolint`
3. Build the Docker image
4. Call the `/version` endpoint and verify it returns the correct value

Security posture is also monitored via the [OpenSSF Scorecard GitHub Action](https://securityscorecards.dev/#using-the-github-action).

## Versioning

This project follows [Semantic Versioning](https://semver.org/). The current release is tagged as `v0.1.0` in this repository.

## Roadmap

This project is developed incrementally, phase by phase, following the [HiveBox project roadmap](https://devopsroadmap.io/projects/hivebox/). Each phase is implemented in its own pull request against `main`.

- [x] Phase 1 — Project setup and planning
- [x] Phase 2 — Initial versioned app (`v0.0.1`), Dockerfile, and local testing workflow
- [x] Phase 3 — REST API endpoints (`/version`, `/temperature`), Docker best practices, CI pipeline
- [ ] Phase 4 — Kubernetes deployment, metrics endpoint
- [ ] Phase 5 — Caching, storage, Helm charts, observability