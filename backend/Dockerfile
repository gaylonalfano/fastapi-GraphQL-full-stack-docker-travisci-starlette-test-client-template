# -- Image you are going to inherit
FROM tiangolo/uvicorn-gunicorn:python3.8-slim

# (optional) Who's maintaining the project
LABEL maintainer="Sebastian Ramirez <tiangolo@gmail.com>"

# Set the Python unbuffered environment variable
# Recommended when running Pythin within Docker containers
# It doesn't allow Python to buffer the outputs. Just prints directly.
# This avoids complications with Docker image when running your Python app.
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

# -- Switch to this new directory (like cd basically) and set as default
# Any application we run from the Docker container will start/run from this directory
WORKDIR /app

# -- Store our dependencies in a requirements.txt file and copy to docker image# -- Switch to this new directory (like cd basically) and set as default
# Any application we run from the Docker container will start/run from this directory

COPY requirements.txt ./
# COPY ./requirements.txt /requirements.txt
# -- Installs our requirements into the Docker image
RUN pip install -r requirements.txt

# -- Copies from local machine /app folder to the /app folder on our image.
# This allows us to copy our code we create and copy to our Docker image.
COPY ./app/ /app

# The container runs but can't access.
# CMD [ "uvicorn", "main:app", "--reload"]

# -- Create a user that is going to run our application using Docker
# The "-D" specifies that the user will ONLY run our process from our project.
# RUN adduser -D user --- ERROR Option d is ambiguous
# RUN adduser --uid 1000 --disabled-password --gecos '' --no-create-home user

# -- Switches Docker to the user we just created. This is for security. Limits their scope.
# If we don't use this then the image will run using the root account.
# That means if somebody compromises our application they can have root access
# to the whole image.
# USER user