# Use an official Python runtime as a base image
FROM python:3.9

# Set the working directory in the container to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Command to run the application when the container starts
CMD ["python", "./Jajanken.py"]

