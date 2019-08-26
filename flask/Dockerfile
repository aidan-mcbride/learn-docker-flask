# Start from base image containing
# Python3.7 installed on Debian Stretch
FROM python:3.7-stretch

# Set the working directory to /app'
# conceptually equivalent to cd'ing into /app
WORKDIR /app

# copy the current directory contents into
# the container at /app
ADD . /app

# Install flask app dependencies
RUN pipenv install

# run the command to start uWSGI server
# see:
# https://docs.docker.com/engine/reference/builder/#cmd
# https://uwsgi-docs.readthedocs.io/en/latest/Configuration.html#loading-configuration-files
CMD ["uwsgi", "app.ini"]
