# pip vs uv

## pip workflow
- Create environment using: python -m venv .venv
- Activate environment.
- Install packages using pip install.
- Generate requirements using pip freeze.

## uv workflow
- Create environment using uv venv.
- Activate environment.
- Install packages using uv pip install.
- Generate requirements using uv pip freeze.

## Comparison
- pip is the traditional Python package manager.
- uv is significantly faster.
- uv provides pip-compatible commands.
- Both can generate requirements.txt.
- Virtual environments isolate project dependencies.