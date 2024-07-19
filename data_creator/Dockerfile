# Use the official Python image as the base image
FROM python:3.11

# Set the working directory inside the container
WORKDIR /app

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Set the entrypoint command to run main.py
CMD ["python", "main.py"]