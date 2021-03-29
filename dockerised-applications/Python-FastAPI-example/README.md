# FastAPI application

This is a simple demonstration of how FastAPI app can be containerised. Anyone can use this code as a template.

There are comments added in the Dockerfile which are self explanatory.

To create the container:
1. Open a terminal and cd into this directory.
2. `docker image build -t fastapi .` <br> 
This command will create a docker image by pulling the latest python image from dockerhub and configure the image to run our FastAPI application. Don't forget to tag your image else the default name will be &lt;none&gt;. On execution of this command, you should see image parts being pulled and dockerfile commands run in new layers.
3. `docker run -p 3565:3565 --name my_fastapi_app fastapi:latest` <br>
This command will start the container and after running this, open `0.0.0.0:3565` and you can see output of your FastAPI application. In the -p flag, port number before : is host port and the latter is container port. Host port can be any free port on your computer but container port must match with the one defined in our dockerfile. It is a good pratice to name containers else docker assigns random names.