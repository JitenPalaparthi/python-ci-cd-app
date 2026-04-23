# Python CI/CD Demo with GitHub Actions and GHCR

This is a complete starter project for a Python application with:

- FastAPI app
- Pytest tests
- Ruff linting
- Mypy type checking
- Pre-commit hooks
- Docker build
- GitHub Actions CI
- GitHub Actions CD to GitHub Container Registry (GHCR)

## Image name

This setup publishes to:

```text
ghcr.io/jitenpalaparthi/python-ci-cd-app
```

Note: GHCR image names are usually lowercase, so `jitenpalaparthi` is used in the image path even though your GitHub username is `JitenPalaparthi`.

## Project structure

```text
.
├── app
│   ├── __init__.py
│   └── main.py
├── tests
│   └── test_main.py
├── .github
│   └── workflows
│       ├── ci.yml
│       └── cd.yml
├── Dockerfile
├── requirements.txt
├── requirements-dev.txt
├── pyproject.toml
├── .pre-commit-config.yaml
└── README.md
```

## Run locally

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements-dev.txt
uvicorn app.main:app --reload
```

Open:

- http://localhost:8000
- http://localhost:8000/docs
- http://localhost:8000/health

## Run quality checks locally

```bash
ruff check .
mypy app tests
pytest -q
```

## Enable pre-commit

```bash
pip install pre-commit
pre-commit install
pre-commit run --all-files
```

## GitHub Actions behavior

### CI workflow

Runs on:

- pull requests
- pushes to `main`, `master`, `develop`

Steps:

1. Install Python dependencies
2. Run Ruff
3. Run Mypy
4. Run Pytest

### CD workflow

Runs on:

- push to `main`
- version tags like `v1.0.0`
- manual trigger

Steps:

1. Build Docker image
2. Log in to GHCR
3. Push image to GHCR

## Important GitHub repo settings

In your GitHub repository:

1. Push this code to a repository.
2. Go to **Settings → Actions → General**.
3. Make sure workflow permissions allow:
   - **Read and write permissions**
4. Save.

This is needed because the CD workflow uses `GITHUB_TOKEN` to push to GHCR.

## Example commands

### Build image locally

```bash
docker build -t python-ci-cd-app .
```

### Run container locally

```bash
docker run -p 8000:8000 python-ci-cd-app
```

### Pull from GHCR later

```bash
docker pull ghcr.io/jitenpalaparthi/python-ci-cd-app:latest
```

### Run from GHCR

```bash
docker run -p 8000:8000 ghcr.io/jitenpalaparthi/python-ci-cd-app:latest
```

## Suggested next improvements

- Add code coverage with `pytest-cov`
- Add security scan with `bandit` and `pip-audit`
- Add semantic version release workflow
- Deploy automatically to Render, Fly.io, EC2, Kubernetes, or Azure Web App
- Add multi-stage Docker build
