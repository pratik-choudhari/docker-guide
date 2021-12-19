### Build image 

```
docker build -t jenkins-docker .
```

### Start container

In order to allow jenkins to deploy docker on host, we have to allow containerised jenkins to communicate with the docker in host, to do this we replace the docker socket file in docker with the one in user.

```
docker run -p 8080:8080 -p 50000:50000 -v /var/jenkins_home:/var/jenkins_home -v /var/run/docker.sock:/var/run/docker.sock --name jenkins -d jenkins-docker
```

Jenkins will load in localhost:8080
