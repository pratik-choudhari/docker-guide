# Dockerfile

Dockerfile is a human-readable text file which tells docker how to build a docker image. Dockerfile most of the time is named as `Dockerfile` whereas a user can name it anything.

Following is the list of most used commands in a dockerfile:

<pre>FROM NAME[:TAG|@DIGEST]</pre>
The <code>FROM</code> instruction tells docker-engine which base image is to be used.<br>
Example: 
<ul>
<li><code>FROM ubuntu:latest</code></li>
<li><code>FROM redis:community-7.0.0-beta</code></li>
</ul>

<br>

<pre>- RUN &lt;COMMAND&gt; (shell form)
- RUN ["EXECUTABLE", "PARAM1", "PARAM2"] (exec form)</pre>
The <code>RUN</code> instruction executes a command in docker container's shell. Default executable for linux is /bin/sh. In shell form, the entire command must be specified after the word <code>RUN</code>, whereas in exec format, the same command is specified as a JSON array. Never mix these two forms together.<br>
Example: 
<ul>
<li><code>RUN apt update</code></li>
<li><code>RUN ["npm", "install"]</code></li>
</ul>

<br>

<pre>EXPOSE &lt;PORT&gt; [&lt;PORT&gt;/PROTOCOL]</pre>
<code>EXPOSE</code> informs docker that the container will be listening on the specified port. Note that this does not mean user can access the app through this port, <code>EXPOSE</code> does not open the port to the host machine, it just serves as a means of documentation to the developer(s).<br>
Example: 
<ul>
<li><code>EXPOSE 5000</code></li>
<li><code>EXPOSE 6622/udp</code></li>
</ul>

<br>

<pre>ENV &lt;KEY&gt;=&lt;VALUE&gt; [&lt;KEY&gt;=&lt;VALUE&gt;...]</pre>
Use the <code>ENV</code> command to set environment variables. Environment variables are a great alternative to explicit variable assignment which includes configuration data and sensitive information. <code>=</code> sign in the instruction can be omitted and replaced by  space.<br>
Example: 
<ul>
<li><code>ENV DB=Mongodb</code></li>
<li><code>ENV WORKERS 10</code></li>
</ul>

<br>

<pre>- CMD &lt;COMMAND&gt; (shell form)
- CMD ["EXECUTABLE", "PARAM1", "PARAM2"] (exec form)
- CMD ["PARAM1", "PARAM2"] (entrypoint default args)</pre>
<code>CMD</code> command is used to provide default arguments for <code>ENTRYPOINT</code> instruction. It is used by docker only if no additional arguments are provided while running the docker container. The main reason <code>CMD</code> is used, is to provide some default arguments in the case where user does not specify any. If a user specifies multiple CMD instructions, only the last instruction will be executed by docker.<br>
Example: 
<ul>
<li><code>CMD ["echo", "linux is the best"]</code> (executes a command)</li>
<li><code>CMD ["-c", "100", "--nodes", "5"]</code> (provides default arguments to ENTRYPOINT command)</li>
</ul>

<br>

<pre>- ENTRYPOINT &lt;COMMAND&gt; (shell form)
- ENTRYPOINT ["EXECUTABLE", "PARAM1", "PARAM2"] (exec form)</pre>
When a container is used as an executable there must be one <code>ENTRYPOINT</code> command in the dockerfile. ENTRYPOINT arguments can not be over-ridden by providing command-line arguments to <code>docker run</code>.<br>
Example:
<ul>
<li><code>ENTRYPOINT ["ps", "aux"]</code> (executes a command)</li>
<li><code>ENTRYPOINT ["gunicorn", "--workers", "2", "test:app"]</code> (start the app and use the container as an executable)</li>
</ul>

<br>

Examples:
- [FastAPI Dockerfile](https://gist.github.com/pratik-choudhari/fb3e45e3e0a116d6db77c696613c4f13)

Learn about Docker images, start the [next lesson](docker_image.md)

Resources:

- (docs)[Dockerfile reference](https://docs.docker.com/engine/reference/builder/)
- (video)[Dockerfile Tutorial - Docker in Practice || Docker Tutorial 10 by TechWorld with Nana](https://www.youtube.com/watch?v=WmcdMiyqfZs)
- (article)[Intro Guide to Dockerfile Best Practices](https://www.docker.com/blog/intro-guide-to-dockerfile-best-practices/)
