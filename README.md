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

# Activate it (PowerShell)
.venv\Scripts\activate

# Upgrade pip and install dependencies
python -m pip install --upgrade pip
pip install -r requirements.txt

# Start FastAPI with Uvicorn (development)
uvicorn src.main:app --reload --host 127.0.0.1 --port 8000

# Open API docs in your browser:
# http://127.0.0.1:8000/docs
```

Notes:

- The `uvicorn` command assumes the FastAPI app instance is named `app` in `backend/src/main.py`.
- For external access, change `--host 127.0.0.1` to `--host 0.0.0.0` (use with caution).

## Running Tests

- Unit tests (run from `backend`):

```powershell
cd backend
.venv\Scripts\activate
python -m pytest ..\tests --cov=src --cov-report=xml
```

- End-to-end tests (Playwright) are kept in `tests/e2e` and should be run in a proper environment with the app running. Example:

```bash
# from repository root
npx playwright test tests/e2e
```

## Development Checklist

- Ensure you run linters and formatters (`flake8`, `black`, `isort`) before committing.
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
