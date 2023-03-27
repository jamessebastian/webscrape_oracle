# Use an official Python runtime as a parent image
FROM python:3.9

# Set the working directory to /app
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .


# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

RUN pip3 install djongo
# Copy the current directory contents into the container at /app
COPY . /app

# Expose port 8000 for the Django development server
EXPOSE 8000

# Start the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]