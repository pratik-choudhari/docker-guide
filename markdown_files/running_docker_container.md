# Starting a Docker container

In a [previous lesson](./docker_image.md), we learned about docker images and now we know that:
<p align="center"><i>Docker images are blueprints of docker containers</i></p>

To bring these blueprints to life is to create a docker container using the `docker run` command. For an instance let's consider we have an image with name `ubuntu:latest` already built onto our system.

<br>

__The command:__
<pre>docker run [OPTIONS] IMAGE_NAME[:TAG|@DIGEST] [COMMAND] [ARGS...]</pre>
Examples: 
<ul>
    <li><code>docker run ubuntu:latest</code></li>
    <li><code>docker run -it -p 5000:80 -e "MODE=DEBUG" my_mongo_image</code></li>
    </ul>

<br>

__Options used in docker run:__

There are a plethora of options available for `docker run` but here we will learn a few keys ones.


<pre>-p HOST_PORT:CONTAINER_PORT[/PROTOCOL]</pre>
The <code>-p</code> option publishes the specified container port to the specified host machine port.<br>
Example: 
<ul>
<li><code>docker run -p 5000:80/tcp my_mongo_image</code></li>
</ul>

<br>

<pre>-i -t</pre>
By default the processes running inside a docker container can not read from the host machine standard input or STDIN. To over come this issue and provide input to the container processes from host machine use the <code>-i</code> flag. The <code>-t</code> flag is used to create a pseudo terminal for our app inside the container, now user can see every prompt from the app straight to the host machine terminal. Both options are used together as <code>-it</code>.<br>
Example: 
<ul>
<li><code>docker run -it ubuntu:latest</code></li>
</ul>

<br>

<pre>-e VAR=VALUE</pre>
The <code>-e</code> option sets environment variables in the container. If the variable in this option are already specified in Dockerfile then ones in dockerfile be overridden. Specifying a variable without any value will use the values from host machine.<br>
Example: 
<ul>
<li><code>docker run -e USER=ADMIN -e PASSWD=hd7632b alpine_image:jimjam</code></li>
</ul>

<br>

<pre>--name CONTAINER_NAME</pre>
Every container is assigned an internal IP address which does not coincide with the host IP space. So, if multiple containers want to communicate then they must contact via the assigned IP address but here we can not guarantee that a container will be assigned the same IP every time, there is an easy workaround this process and it is to contact a container via it's name. Docker assigns a random name to container, unless specified. Providing a name explicitly, creates an entry for the conatiner IP and the name inside docker's embedded DNS. <br>
Example: 
<ul>
<li><code>docker run --name logger_container alpine_image:jimjam</code></li>
</ul>

<br>

<pre>--network NETWORK_NAME</pre>
Communication between containers can be managed seemlessly using --network. Docker has 4 types of network to choose from these include host, bridge, none, and user-defined. Default is bridge.<br>
Example: 
<ul>
<li><code>docker run --network host alpine_image:jimjam</code></li>
<li><code>docker run --network custom_subnet1 alpine_image:jimjam</code></li>
<li><code>docker run --network none alpine_image:jimjam</code></li>
</ul>

<br>

<pre>-v VOLUME_NAME:CONTAINER_PATH</pre>
The <code>-v</code> flag is used to mount a volume in the docker container. Value for <code>-v</code> is the volume name and path inside container seperated by a <code>:</code><br>
Example: 
<ul>
<li><code>docker run -v vol2:/code/app alpine_image:jimjam</code></li>
</ul>

<br>

Next, see how data is managed in docker, [click here](docker_data_storage.md)

Resources:

- (docs)[docker run reference](https://docs.docker.com/engine/reference/run/)
- (video)[What is a container in Docker](https://www.youtube.com/watch?v=HMAoJoSJCyk)
