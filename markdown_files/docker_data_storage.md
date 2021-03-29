# Data Storage in Docker

## The data layers:

Every docker container has 2 layers, the first layer is a Read-only layer aka the docker image and the second layer is a Writeable layer aka the container storage. 

## Container data management:

When a container is stoppped all of the data written inside the container is stored on the host machine disk. On restarting the container this data can be accessed again. But when a container is removed the data created by the container is also deleted permanently. Therefore, data does not persist on the host machine.

## Achieving data persistence:

To save data on the host disk, the container can be mounted to a location on the host machine. There are 3 types of mounts in docker:
- bind mount: A bind mount can save data from a docker container to any location on the host file system.
- volume: Easiest option available. Data written into docker volumes is stored in `/var/lib/docker/volumes/` (on Linux). Volumes can be mounted into multiple containers.
- tmpfs: tmpfs is a temporary file storage system which stores data in a volatile memory i.e. RAM. Therefore, this option can not be counted as true persistence.

<br>

## Docker volumes:

__Create a volume:__

<pre>docker volume create custom_vol0</pre>
Creates a volume in <code>/var/lib/docker/volumes</code>

<br>

__Delete a volume:__

<pre>docker volume rm custom_vol0</pre>
Deletes the volume from <code>/var/lib/docker/volumes</code>

<br>

__Inspect a volume:__

<pre>docker volume inspect custom_vol0</pre>
Shows in-depth information about the volume in a JSON array format.

<br>

## Mounting a volume:

A volume can be mounted via docker-cli or while creating the docker image by including the volume information in Dockerfile.

1. dockerfile: By the using `VOLUME` command in a dockerfile, we tell docker to mount the volume everytime it's container is run.

2. Thorugh docker-cli: Including the `-v` flag with other mounting information in `docker run` command, volumes can be mounted at run-time. AN alternative to `-v` is to use it's verbose version `--mount`. The only difference between them is that `--mount` argument names are more verbose and easy to understand.

Example:

- `docker run --name devtest -v myvol2:/app nginx:latest`
- `docker run --name devtest --mount source=myvol2,target=/app nginx:latest`

Resources:

- (docs)[docker volumes](https://docs.docker.com/storage/volumes/)
