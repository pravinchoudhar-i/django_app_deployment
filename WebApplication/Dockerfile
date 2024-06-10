FROM python:3.10.5-slim-buster

# Set debconf to noninteractive mode
ENV DEBIAN_FRONTEND=noninteractive
ADD WebApplication/requirements.txt /WebApplication/requirements.txt

RUN apt-get update \
    && apt-get -y install libpq-dev gcc \
    && python -m venv /env \
    && /env/bin/pip install --upgrade pip \
    && /env/bin/pip install --no-cache-dir -r /WebApplication/requirements.txt 

ADD WebApplication /tw_doc_gen
WORKDIR /WebApplication

# Copy the .env file
COPY .env /WebApplication/.env

ENV VIRTUAL_ENV /env
ENV PATH /env/bin:$PATH

EXPOSE 8000

CMD ["gunicorn", "--bind", ":8000", "--workers", "3", "WebApplication.wsgi:application"]

