FROM python:3.11-slim-bookworm

# set env vars
ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

#set working directory
WORKDIR /app

# pip install dependencies
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# copy project
COPY . .