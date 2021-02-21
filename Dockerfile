FROM python:3.6

ENV PYTHONUNBUFFERED 1

RUN mkdir /notes_api

WORKDIR /notes_api

ADD . /notes_api/

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt
