FROM python:3.11-slim


RUN apt-get update && \
    apt-get upgrade -y

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /code

# Install dependencies
COPY pyproject.toml poetry.lock /code/
RUN pip install poetry==1.6.1 && poetry config virtualenvs.create false && --no-interaction --no-ansi --no-root --no-dev

# Copy project
COPY . /code/

EXPOSE 8000

# Command to run the application
CMD ["uvicorn", "server:app", "--host", "0.0.0.0", "--port", "8000"]
