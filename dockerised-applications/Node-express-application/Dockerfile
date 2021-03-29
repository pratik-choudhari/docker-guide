# use the latest node image i.e 15.12 of size ~310MB
FROM node:latest

# create a new folder inside our container
RUN mkdir /code

# set /code as working directory inside the container
WORKDIR /code

# copy everything from host machine folder where this Dockerfile resides into /code in our container
COPY . /code/

# install dependencies
RUN npm install

# acts as a documentation for other developers, doesn't actually publishes the port
EXPOSE 3000

# start app with entrypoint command
# this port will be published using -p argument in docker run command
ENTRYPOINT ["npm", "start"]