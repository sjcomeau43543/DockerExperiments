This was an experiment to test what docker containers would continue running if they were "revived" through running `docker start <container>`

A docker container that will continuously run when invoked will have one of the following qualities.
1. The docker container is running a program that will accept commands
2. The docker container is opening a port that will accept commands 

For example:
Docker Splunk will continuously run when invoked because of the fact that it opens an HTTP port that will accept commands