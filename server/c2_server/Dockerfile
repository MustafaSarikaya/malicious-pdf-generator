FROM python:3.11.0

# Set the working directory
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Expose the port the app runs on
EXPOSE 8080

# Define the command to run the application
CMD ["python", "c2_server.py"]