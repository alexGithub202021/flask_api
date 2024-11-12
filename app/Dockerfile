# Use the official Python image from Docker Hub
FROM arm64v8/python:latest
# FROM arm64v8/python:2.7

USER root

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed dependencies specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Run app.py when the container launches
CMD ["python3", "app.py"]
# # ENTRYPOINT [ "python3", "-m", "debugpy", "--listen", "0.0.0.0:5678", "--wait-for-client"]