# Lockscript

## Educational Purpose

This project was created primarily for **educational and learning purposes**.  
While it is well-structured and could technically be used in production, it is **not intended for commercialization**.  
The main goal is to explore and demonstrate best practices, patterns, and technologies in software development.

## Getting Started

1. Clone the repository
2. Go to the repository folder and execute: `python -m venv venv`
3. Execute in Windows: `venv\Scripts\activate`
4. Execute in Linux/Mac: `source venv/bin/activate`
5. Execute: `pip install -r requirements.txt`
6. Execute: `pip install -r requirements.dev.txt`
7. Execute: `pip install -r requirements.test.txt`
8. Use `python app.py` or `python -m src` to execute the program

### Pre-Commit for Development

1. Once you're inside the virtual environment, let's install the hooks specified in the pre-commit. Execute: `pre-commit install`
2. Now every time you try to commit, the pre-commit lint will run. If you want to do it manually, you can run the command: `pre-commit run --all-files`

## Description

**Lockscript** is a desktop application built with Python and Tkinter that lets you encrypt and decrypt text files directly from a graphical interface — no terminal knowledge required.

**How it works:**

The user selects a text file using the built-in file importer. Once a file is loaded, two actions are available: **Encrypt** and **Decrypt**. Encryption applies a Caesar-style character shift (+1) to every character in the file, transforming readable text into an unreadable form. Decryption reverses that process (-1), restoring the original content — as long as the file was previously encrypted with this same application.

**Key characteristics:**

- **File-based**: works directly on `.txt` files stored on disk. The encrypted output overwrites (or is saved alongside) the original file.
- **No external dependencies for core logic**: the encryption engine is self-contained and requires no third-party cryptography libraries.
- **Error-aware UI**: invalid file paths, unsupported formats, or missing selections trigger descriptive dialog popups rather than silent failures, making the experience beginner-friendly.
- **Environment-aware**: supports `development`, `production`, and `testing` configurations via a `.env` file, enabling clean separation between runtime contexts.
- **Distributable**: the app can be packaged into a standalone executable (`.exe` on Windows, binary on Linux/Mac) using PyInstaller, so end users do not need Python installed.

**Intended use:**

Lockscript is designed as a lightweight, educational tool to demonstrate how a full Python desktop application can be structured — covering UI, service layer, error handling, configuration management, testing, linting, and build pipelines — all within a single cohesive project.

## Technologies used

1. Python >= 3.11
2. Tkinter

## Libraries used

#### Requirements.txt

```
python-dotenv==1.0.1
```

#### Requirements.dev.txt
```
pre-commit==4.3.0
pip-audit==2.7.3
ruff==0.11.12
```

#### Requirements.test.txt

```
pytest==8.4.2
pytest-env==1.1.5
pytest-cov==4.1.0
pytest-timeout==2.3.1
pytest-xdist==3.5.0
```

#### Requirements.build.txt

```
pyinstaller==6.16.0
```

## Portfolio Link

[`https://www.diegolibonati.com.ar/#/project/lockscript`](https://www.diegolibonati.com.ar/#/project/lockscript)

## Testing

1. Go to the repository folder
2. Execute: `python -m venv venv`
3. Execute in Windows: `venv\Scripts\activate`
4. Execute in Linux/Mac: `source venv/bin/activate`
5. Execute: `pip install -r requirements.txt`
6. Execute: `pip install -r requirements.test.txt`
7. Execute: `pytest --log-cli-level=INFO`

## Build

You can generate a standalone executable (`.exe` on Windows, or binary on Linux/Mac) using **PyInstaller**.

### Windows

1. Go to the repository folder
2. Activate your virtual environment: `venv\Scripts\activate`
3. Install build dependencies: `pip install -r requirements.build.txt`
4. Create the executable: `pyinstaller app.spec`

Alternatively, you can run the helper script: `build.bat`

### Linux / Mac

1. Go to the repository folder
2. Activate your virtual environment: `source venv/bin/activate`
3. Install build dependencies: `pip install -r requirements.build.txt`
4. Create the executable: `pyinstaller app.spec`

Alternatively, you can run the helper script: `./build.sh`

## Security Audit

You can check your dependencies for known vulnerabilities using **pip-audit**.

1. Go to the repository folder
2. Activate your virtual environment
3. Execute: `pip install -r requirements.dev.txt`
4. Execute: `pip-audit -r requirements.txt`

## Env Keys

1. `ENVIRONMENT`: Defines the application environment. Accepts `development`, `production`, or `testing`.

```
ENVIRONMENT=development
```

## Known Issues

None at the moment.