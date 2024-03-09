#start docker kernal + python 
FROM python:3.11.7-slim-bullseye


# show logs :python 
ENV PYTHONUNBUFFERED = 1 

#update kernal + install 
RUN apt-get update && apt-get -y install gcc libpq-dev

#folder for my project
WORKDIR /app

#copy requirements
COPY requirments.txt /app/requirments.txt

#install req
RUN pip install -r /app/requirments.txt

# copy all project file
COPY . /app/    