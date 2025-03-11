FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Install Poetry
RUN curl -sSL https://install.python-poetry.org | python3 -

# Add Poetry to PATH
ENV PATH="${PATH}:/root/.local/bin"

# Copy pyproject.toml, poetry.lock, and README.md (needed for package installation)
COPY pyproject.toml poetry.lock* README.md ./

# Configure Poetry to not create a virtual environment
RUN poetry config virtualenvs.create false

# Install dependencies using --no-root flag
RUN poetry install --without dev --no-interaction --no-root

# Copy the rest of the application
COPY . .

# Set the entrypoint
ENTRYPOINT ["python", "src/main.py"]