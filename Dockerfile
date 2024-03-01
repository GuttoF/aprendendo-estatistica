FROM python:3.9.18-slim

# Install system dependencies required for Python 
RUN apt-get update && apt-get install -y \
    gcc \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*



# Install Poetry
RUN pip install poetry

# Set the working directory in the container
WORKDIR /app

# Copy pyproject.toml and poetry.lock to the container
COPY pyproject.toml poetry.lock* /app/

# Configure Poetry
RUN poetry config virtualenvs.create false

RUN poetry install --no-interaction --no-ansi

# Copy the rest of your application's code into the container
COPY . /app

EXPOSE 8501

# Command to run the application
CMD ["streamlit", "run", "aprendendo_estatistica/streamlit_app.py", "--server.port=8501"]


