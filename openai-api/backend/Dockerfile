# Use the official Python image from the Docker Hub
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /

# Copy the requirements file into the container
COPY ./backend/requirements.txt ./backend/requirements.txt

# Install the dependencies
RUN pip install --no-cache-dir -r ./backend/requirements.txt

# Copy the rest of the application code into the container
COPY ./backend/src/ ./backend/src/
COPY ./backend/data/ ./backend/data/

# Copy the config files into the container
COPY ./config/.env.dev ./config/.env.dev

# Set the entry point for the container
CMD ["python", "backend/src/app/app.py"]