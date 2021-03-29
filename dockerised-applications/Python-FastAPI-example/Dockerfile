# use the latest python image which is 3.10 with size of ~320MB
FROM python:latest

# create a new folder inside our container
RUN mkdir /code

# set /code as working directory inside the container
WORKDIR /code

# copy everything from host machine folder where this Dockerfile resides into /code in our container
COPY . /code/

# install fastapi
RUN pip3 install -r requirements.txt

# acts as a documentation for other developers, doesn't actually publishes the port
EXPOSE 3565

# start app with entrypoint command, specify the host and port
# this port will be published using -p argument in docker run command
ENTRYPOINT ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "3565"]