# Use the official Python image as the base image
FROM python:3.11

# Set the working directory inside the container
WORKDIR /app

# echo the contents of the /app folder for troubleshooting
RUN echo "Contents of /app after COPY:" && ls -la /app

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Set the entrypoint command to run main.py
CMD ["sh", "-c", "ls -la /app && python main.py"]