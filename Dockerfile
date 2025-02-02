# Use official Python runtime as a base image
FROM python:3.12

# Set environment variable to avoid Python buffering logs
ENV PYTHONUNBUFFERED 1

# Set the working directory to /app inside the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt /app/

# Install the dependencies from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project directory to /app inside the container
COPY . /app/

# Expose the port that Django will run on (default 8000)
EXPOSE 8000

# Run the Django development server (change the command if needed)
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
