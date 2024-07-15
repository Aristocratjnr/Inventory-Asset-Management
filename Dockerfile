# Use an official Python runtime as a parent image
FROM python:3.10

# Set the working directory in the container
WORKDIR /djangoproject

# Copy the current directory contents into the container at /schoolmanagement/
COPY . /djangoproject/

# Create a virtual environment and install dependencies
RUN python -m venv venv && \
    /bin/bash -c "source venv/bin/activate && \
    pip install --upgrade pip && \
    pip install -r requirements.txt"

# Run migrations and start the Django development server within the virtual environment
CMD /bin/bash -c "source venv/bin/activate && \
    python manage.py makemigrations && \
    python manage.py migrate && \
    python manage.py runserver 0.0.0.0:8000 --noreload"