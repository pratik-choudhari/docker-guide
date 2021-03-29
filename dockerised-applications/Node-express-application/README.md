# Node express application

This is a simple demonstration of how a node app can be containerised. Anyone can use this code as a template.

There are comments added in the Dockerfile which are self explanatory.

To create the container:
1. Open a terminal and cd into this directory.
2. `docker image build -t node_app .` <br> 
This command will create a docker image by pulling the latest node image from dockerhub and configure the image to run our node application. Don't forget to tag your image else the default name will be &lt;none&gt;. On execution of this command, you should see image parts being pulled and dockerfile commands run in new layers.
3. `docker run -p 3000:3000 --name node_app_cont node_app:latest` <br>
This command will start the container and after running this, open `localhost:3000` and you can see output of your node application. In the -p flag, port number before : is host port and the latter is container port. Host port can be any free port on your computer but container port must match with the one defined in our dockerfile. It is a good pratice to name containers else docker assigns random names.