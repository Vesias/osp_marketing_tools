# Start with a base image that has Python and uv pre-installed
FROM ghcr.io/astral-sh/uv:python3.12-bookworm-slim AS uv

# Set the working directory
WORKDIR /app

# Enable bytecode compilation
ENV UV_COMPILE_BYTECODE=1

# Specify the UV link mode
ENV UV_LINK_MODE=copy

# Copy project files
COPY . /app/

# Use uv to install dependencies and sync project
RUN uv sync --python-source=/usr/local/bin/python3 --frozen --no-dev
RUN uv pip install -e .

# Start a new stage to keep the final image small
FROM python:3.12-slim-bookworm

# Create non-root user
RUN groupadd -r app && useradd -r -g app app

# Set the working directory
WORKDIR /app

# Copy project files and virtual environment
COPY --from=uv --chown=app:app /app /app
COPY --from=uv --chown=app:app /app/.venv /app/.venv

# Update permissions
RUN chown -R app:app /app

# Set environment variables
ENV PATH="/app/.venv/bin:$PATH"
ENV PYTHONPATH="/app:$PYTHONPATH"

# Switch to non-root user
USER app

# Set the entry point to run the MCP server
ENTRYPOINT ["python", "-m", "osp_marketing_tools.server"]
