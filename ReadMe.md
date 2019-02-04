This will experiment with docker containers to test different hypotheses.

## Background

### Images

This describes the images that were used in this project.

| Image       | Description | 
| ----------- | ----------- |
| alpine      | alpine is a Linux distribution based on busybox |
| centos      | centos is a Linux distribution based on RedHat |
| hello-world | hello-world is a tester to test the docker setup on the computer and print hello world |
| nginx       | nginx is a reverse proxy server |
| splunk      | splunk is a fully functional splunk setup (with a web server) |




## Part 1

This was an experiment to test what docker containers would continue running if they were "revived" through running `docker start <container>`

### Hypothesis

A docker container that will continuously run when invoked will have one of the following qualities.
1. The docker container is running a program that will accept commands
2. The docker container is opening a port that will accept commands 

For example:
Docker Splunk will continuously run when invoked because of the fact that it opens an HTTP port that will accept commands

### Methodology

To test this, I created many different containers with different build images and different options put into the images. To test simple programs I used `alpine` and `hello-world`. To test running a program on an image I used `centos` and `/bin/bash`. To test opening ports and web servers I used `nginx` and `splunk`. 

I also tested if docker command line options to `run` would affect the outcome of certain images. I tested `--detach` which claims to keep containers running in the background. **TODO MORE

After creating the containers, I print the status of them, stop them, and start them again.
Finally, I check the status one more time to see if they started running and were "revived".

### Testing
| Image       | Options | Program | Outcome | TODO
| ----------- | ------- | ------- | ------- |
| alpine      | None | None | ------- |
| alpine      | --detach | None | ------- |
| centos      | --detach | /bin/bash | ------- |
| hello-world | None | None | ------- | 
| nginx       | --detach | None | ------- | 
| splunk      | --detach (and some env variables) | None | ------- | 



## Part 2

This was an experiment to test what causes docker containers to take so long to stop using `docker stop <container>`

### Hypothesis

1. The first hypothesis is that the longer they are running the longer it will take to stop
2. The second hypothesis is that the more complex they are (ex opening port, setting credentials) the longer it will take to stop

### Methodology
TODO
### Testing

TODO
