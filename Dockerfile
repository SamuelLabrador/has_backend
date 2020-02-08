FROM python:3.7
ENV PYTHONNINBUFFERED 1

# Create and set working directory for our source code
RUN mkdir /backend
WORKDIR /backend/

COPY requirements.txt /backend
RUN pip install -r requirements.txt

COPY . /backend