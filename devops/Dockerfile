# Use a lightweight Python base image
FROM python:3.12.6-slim

# Set the working directory inside the container
WORKDIR /app


# Copy and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the full Django project
COPY . .

# Expose Django’s port
EXPOSE 8000

# Run Django app
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

