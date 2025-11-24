# Tasks DevSecOps

## Project Description

This is a simple FastAPI-based web application for managing tasks. It supports the basic operations:

- Create a task (POST)
- Read tasks (GET)
- Delete a task (DELETE)

The application is designed with security in mind and includes automated testing and CI/CD pipeline. API documentation (interactive Swagger UI) is available at `/docs` when the server is running.

## Quick Start (Run Locally)

Follow these steps to run the project locally.

```bash
# 1) Clone repository
git clone https://github.com/YOUR_USERNAME/tasks_devsecops.git
cd tasks_devsecops

# 2) Create a virtual environment
python -m venv venv

# 3) Activate the virtual environment
# Windows (PowerShell or cmd)
venv\Scripts\activate

# Linux / macOS
# source venv/bin/activate

# 4) (Optional) Upgrade pip and install dependencies
python -m pip install --upgrade pip
pip install -r requirements.txt

# 5) Start FastAPI with Uvicorn (development)
uvicorn src.main:app --reload --host 127.0.0.1 --port 8000

# 6) Open API docs in your browser:
# http://127.0.0.1:8000/docs
```

Notes:

- The `uvicorn` command assumes the FastAPI app instance is named `app` in `src/main.py`.
- For external access, change `--host 127.0.0.1` to `--host 0.0.0.0` (use with caution).

## Running Tests

Run the automated test suite and generate coverage XML:

```bash
python -m pytest tests/unit --cov=src --cov-report=xml
```

```bash
npx playwright test tests/e2e
```

## Security

For details on security requirements, identified threats, and mitigation strategies, see the security analysis document:
[SECURITY-ANALYSIS.md](./SECURITY-ANALYSIS.md)

## API Documentation

Interactive docs are available at:

- Swagger UI: `/docs`
- ReDoc: `/redoc` (if enabled)

## Contributing

Contributions are welcome. Please:

- Open issues for bugs or feature requests.
- Submit pull requests with clear descriptions and tests where applicable.

## License

This project is licensed under the terms in the `LICENSE` file.

## Authors / Maintainers

- Repository owner: `Cameloasa` (see GitHub repo)
