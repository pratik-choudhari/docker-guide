Docker is built to manage containers, therefore it is important to understand the term `containers`

# What is a container?

In today's date software development rate has sky rocketed but this has introduced discrepancies in terms of environment configuration, application isolation and avoiding resource access conflicts. 

A solution for this problem is to use __Virtual Machines__. A Virtual Machine runs an instance of some Operating System and the host machine hardware is virtualised by a bare metal hypervisor(a software resposible for allocation of resources to virtual machines). Here's how a VM is set up.

<center><img src="../images/virtual_machines_architecture.jpg" width=300></img></center>

The reason VMs are not always required to run our applications is that:
- Creation of a VM takes time
- Booting a VM takes time too
- Big OS sizes
- Install dependencies from scratch
- Inability to share a VM instance and recreate exact environment
- Hardware resource wastage

Soon __containers__ were introduced and they made it much easy to develop and deploy software applications. These containers are created via a software which runs on the host machine serving certain OS. 

*__Here, we do not virtualise hardware but we virtualise the Operating System__*

Here's how containers are set up.

<center><img src="../images/container_architecture.jpg" width=250></img></center>

Containers do not run a complete OS, they operate on kernels. Kernel is a core program in any OS that has complete control over all processes. Size of these kernels are far less as compared to that of an entire OS. For instance, Ubuntu 18.04 LTS is of 2.00 GB whereas Ubuntu docker image is of 27.25 MB only.

Containers allowed developers to recreate an environment free of all dependency conflicts. Containers run on-demand, they boot quickly and only use resources as and when needed.

<br>

# What is docker?

Before diving into docker commands and deploying docker containers, let us first understand `What is docker?`


Docker started as an open-source project in 2013 and to put it in the simplest terms, Docker is nothing but a software that helps a developer create and manage containers.

Docker components:

- Dockerfile: A Dockerfile is a simple human-readable text file that instructs docker how to build a docker image. Each line in this file is a command in the form `[INSTRUCTION] [COMMAND]`.

- Docker image: Docker images are a blueprint of docker containers. It contains information about which software the container will run and how. Docker images are built using Dockerfile.

- Docker container: If docker image is a blueprint then docker container is an instance of these blueprints. Docker container takes the specifications from docker image and executes them to create a environment ready to run you application.

