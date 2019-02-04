This will experiment with docker containers to test different hypotheses.

## Background

### Images

This describes the images that were used in this project.

| Image | Description |
| ----- | ----------- |



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


### Testing



## Part 2

This was an experiment to test what causes docker containers to take so long to stop using `docker stop <container>`

### Hypothesis

1. The first hypothesis is that the longer they are running the longer it will take to stop
2. The second hypothesis is that the more complex they are (ex opening port, setting credentials) the longer it will take to stop

### Methodology

### Testing


