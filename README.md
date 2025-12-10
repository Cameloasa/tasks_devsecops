# Tasks DevSecOps

## Project Description

Tasks DevSecOps is a small FastAPI application that models a common admin/user workflow:

- An admin creates tasks and assigns them to users.
- A user can list their assigned tasks and view task details.
- Admins can also delete tasks or update task state as needed.

The app focuses on simple role-based behavior (admin vs. user), straightforward API endpoints, and automatic CI checks. Interactive API documentation is available at `/docs` when the server is running.

## Key Endpoints (example)

- `POST /tasks` — Create a new task (admin only).
- `GET /tasks` — List tasks (admin sees all, user sees assigned tasks).
- `GET /tasks/{id}` — Get task details.
- `DELETE /tasks/{id}` — Delete a task (admin only).

Authentication and authorization are assumed to be in place (e.g., token-based or role checks). Adjust the implementation to match your security requirements.

## Quick Start (Run Locally)

Run the backend from the `backend` folder.

```powershell
# From repository root
cd backend

# Create a virtual environment
python -m venv .venv

## Quick Start (Run Locally)

This repository contains two main pieces:

- `backend` — Python FastAPI application (uses an isolated virtual environment in `backend/.venv`).
- `frontend` — Vite + React frontend (Node.js / npm).

Follow these steps to run both locally (Windows PowerShell examples). Adjust commands for your shell if needed.

Backend (PowerShell)

```powershell
# from repository root
cd backend

# Create an isolated virtual environment (keeps packages inside backend/.venv)
python -m venv .venv

# Activate venv (PowerShell)
.venv\Scripts\Activate.ps1

# Confirm python points to the backend venv
python -c "import sys; print(sys.executable)"

# Upgrade pip and install dependencies
python -m pip install --upgrade pip
pip install -r requirements.txt

# Start FastAPI with Uvicorn (development)
# The app instance should be named `app` in `backend/src/main.py`
uvicorn src.main:app --reload --host 127.0.0.1 --port 8000

# Open API docs in your browser:
# http://127.0.0.1:8000/docs
```

Frontend (PowerShell)

```powershell
# from repository root
cd frontend

# Install Node dependencies
npm ci

# (Optional) Install Playwright browsers for e2e tests
npx playwright install

# Start development server (Vite)
npm run dev

# Open the app (default Vite port is 5173):
# http://localhost:5173
```

Notes:

- The backend virtual environment is created inside `backend/.venv` so the rest of the repo stays clean. Always activate it before running Python commands for the backend.
- For Linux/macOS use `python -m venv .venv` and `source .venv/bin/activate`.
- For external access, change the `--host` in the `uvicorn` command to `0.0.0.0` (use with caution).

## Running Tests

Backend unit tests (PowerShell)

```powershell
cd backend
.venv\Scripts\Activate.ps1
python -m pytest ..\tests --cov=src --cov-report=xml
```

Frontend end-to-end tests (Playwright)

Playwright tests live in `tests/e2e` (if present). Before running Playwright tests in CI or locally:

1. Ensure the backend is running (see Quick Start -> Backend).
1. Install Playwright browsers (once):

```powershell
cd frontend
npx playwright install --with-deps
```

1. Run Playwright tests from the repository root (this runs JS/TS Playwright tests):

```bash
# from repository root
npx playwright test tests/e2e
```

If your e2e tests are Python-based (httpx or Playwright Python), run them from the backend venv and ensure the server is running.

## Development Checklist

- Backend linting & formatting:

```powershell
cd backend
.venv\Scripts\Activate.ps1
python -m flake8 src/
python -m black src/  # or run black as needed
python -m isort src/
```

- Frontend linting:

```bash
cd frontend
npm ci
npm run lint
```

- Add unit tests under `tests/unit` and e2e flows under `tests/e2e` when implementing features.

## Security

See `SECURITY-ANALYSIS.md` for identified threats and recommended mitigations.

## Contributing

- Open issues for bugs or feature requests.
- Submit pull requests with clear descriptions and tests where applicable.

## License

This project is licensed under the terms in the `LICENSE` file.

## Maintainers

- Repository owner: `Cameloasa`

