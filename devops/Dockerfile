# Use a lightweight Python base image
FROM python:3.12.6-slim

# Set the working directory inside the container
WORKDIR /app

<<<<<<< Updated upstream
# Copy and install dependencies
COPY ./requirements.txt /app/
=======
# Copy requirements.txt first to leverage Docker caching
COPY requirements.txt .

# Install dependencies
>>>>>>> Stashed changes
RUN pip install --no-cache-dir -r requirements.txt

# Copy the full Django project
COPY . /app/

# Expose Django’s port
EXPOSE 8000

# Run Django app
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
