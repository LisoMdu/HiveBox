[![Dynamic DevOps Roadmap](https://img.shields.io/badge/Dynamic_DevOps_Roadmap-559e11?style=for-the-badge&logo=Vercel&logoColor=white)](https://devopsroadmap.io/getting-started/)
[![Community](https://img.shields.io/badge/Join_Community-%23FF6719?style=for-the-badge&logo=substack&logoColor=white)](https://newsletter.devopsroadmap.io/subscribe)
[![Telegram Group](https://img.shields.io/badge/Telegram_Group-%232ca5e0?style=for-the-badge&logo=telegram&logoColor=white)](https://t.me/DevOpsHive/985)
[![Fork on GitHub](https://img.shields.io/badge/Fork_On_GitHub-%2336465D?style=for-the-badge&logo=github&logoColor=white)](https://github.com/DevOpsHiveHQ/devops-hands-on-project-hivebox/fork)

# HiveBox - DevOps End-to-End Hands-On Project

<p align="center">
  <a href="https://devopsroadmap.io/projects/hivebox" style="display: block; padding: .5em 0; text-align: center;">
    <img alt="HiveBox - DevOps End-to-End Hands-On Project" border="0" width="90%" src="https://devopsroadmap.io/img/projects/hivebox-devops-end-to-end-project.png" />
  </a>
</p>

> [!CAUTION]
> **[Fork](https://github.com/DevOpsHiveHQ/devops-hands-on-project-hivebox/fork)** this repo, and create PRs in your fork, **NOT** in this repo!

> [!TIP]
> If you are looking for the full roadmap, including this project, go back to the [getting started](https://devopsroadmap.io/getting-started) page.

This repository is the starting point for [HiveBox](https://devopsroadmap.io/projects/hivebox/), the end-to-end hands-on project.

You can fork this repository and start implementing the [HiveBox](https://devopsroadmap.io/projects/hivebox/) project. HiveBox project follows the same Dynamic MVP-style mindset used in the [roadmap](https://devopsroadmap.io/).

The project aims to cover the whole Software Development Life Cycle (SDLC). That means each phase will cover all aspects of DevOps, such as planning, coding, containers, testing, continuous integration, continuous delivery, infrastructure, etc.

Happy DevOpsing ♾️

## Before you start

Here is a pre-start checklist:

- ⭐ <a target="_blank" href="https://github.com/DevOpsHiveHQ/dynamic-devops-roadmap">Star the **roadmap** repo</a> on GitHub for better visibility.
- ✉️ <a target="_blank" href="https://newsletter.devopsroadmap.io/subscribe">Join the community</a> for the project community activities, which include mentorship, job posting, online meetings, workshops, career tips and tricks, and more.
- 🌐 <a target="_blank" href="https://t.me/DevOpsHive/985">Join the Telegram group</a> for interactive communication.

## Preparation

- [Create GitHub account](https://docs.github.com/en/get-started/start-your-journey/creating-an-account-on-github) (if you don't have one), then [fork this repository](https://github.com/DevOpsHiveHQ/devops-hands-on-project-hivebox/fork) and start from there.
- [Create GitHub project board](https://docs.github.com/en/issues/planning-and-tracking-with-projects/creating-projects/creating-a-project) for this repository (use `Kanban` template).
- Each phase should be presented as a pull request against the `main` branch. Don’t push directly to the main branch!
- Document as you go. Always assume that someone else will read your project at any phase.
- You can get senseBox IDs by checking the [openSenseMap](https://opensensemap.org/) website. Use 3 senseBox IDs close to each other (you can use the following [5eba5fbad46fb8001b799786](https://opensensemap.org/explore/5eba5fbad46fb8001b799786), [5c21ff8f919bf8001adf2488](https://opensensemap.org/explore/5c21ff8f919bf8001adf2488), and [5ade1acf223bd80019a1011c](https://opensensemap.org/explore/5ade1acf223bd80019a1011c)). Just copy the IDs, you will need them in the next steps.

<br/>
<p align="center">
  <a href="https://devopsroadmap.io/projects/hivebox/" imageanchor="1">
    <img src="https://img.shields.io/badge/Get_Started_Now-559e11?style=for-the-badge&logo=Vercel&logoColor=white" />
  </a><br/>
</p>

---

## Implementation

# HiveBox

A scalable RESTful API project built around [openSenseMap](https://opensensemap.org/) data, customized to help beekeepers monitor environmental conditions. This project is being built incrementally as part of the [DevOps Roadmap HiveBox project](https://devopsroadmap.io/projects/hivebox/).

## Project Status

**Current version:** `v0.0.1` (Phase 2)

At this stage, the application is intentionally minimal: it simply prints its current version number and exits. This establishes the foundation — versioning, containerization, and a documented testing workflow — that later phases will build on.

## Prerequisites

To build and run this project, you'll need:

- [Git](https://git-scm.com/)
- [Docker](https://www.docker.com/)
- (Optional, for running without Docker) Python 3.x

## Project Structure

- `app.py` — main application entry point; contains the function that prints the app version
- `requirements.txt` — Python dependencies (minimal at this stage)
- `Dockerfile` — defines how the app is containerized
- `.dockerignore` / `.gitignore` — exclude unnecessary files from the image and repository

## Running Locally (without Docker)

1. Clone this repository and navigate into the project directory.
2. (Optional) Create and activate a Python virtual environment.
3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
4. Run the application:
   ```
   python app.py
   ```

**Expected output:** the application prints its current version (`0.0.1`) to the terminal and exits.

## Building and Running with Docker

1. Build the Docker image:
   ```
   docker build -t hivebox:0.0.1 .
   ```
2. Run a container from the image:
   ```
   docker run hivebox:0.0.1
   ```

**Expected output:** the container prints `0.0.1` to the terminal, then exits cleanly (exit code `0`).

## Testing

To verify this version of the application works as expected:

1. Build the Docker image as shown above.
2. Run the container.
3. Confirm the printed output matches the version defined in `app.py`.
4. Confirm the container exits on its own after printing the version (no manual stop required).

## Versioning

This project follows [Semantic Versioning](https://semver.org/). The current release is tagged as `v0.0.1` in this repository.

## Roadmap

This project is developed incrementally, phase by phase, following the [HiveBox project roadmap](https://devopsroadmap.io/projects/hivebox/). Each phase is implemented in its own pull request against `main`.

- [x] Phase 1 — Project setup and planning
- [x] Phase 2 — Initial versioned app (`v0.0.1`), Dockerfile, and local testing workflow
- [ ] Phase 3 — REST API endpoints (`/version`, `/temperature`), CI pipeline
- [ ] Phase 4 — Kubernetes deployment, metrics endpoint
- [ ] Phase 5 — Caching, storage, Helm charts, observability