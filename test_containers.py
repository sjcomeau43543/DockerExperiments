from Container import Container
import time

def setup_containers():
    containers = []

    # create some containers with differing attributes

    # alpine is a Linux distribution based on busybox
    alpi = Container('alpi', 'alpine', None) # stripped container, no options
    alpi.run([])
    containers.append(alpi)

    alpidetached = Container('alpidetached', 'alpine', None) # detached container, no program
    alpidetached.run(['--detach'])
    containers.append(alpidetached)

    alpidetachedtty = Container('alpidetachedtty', 'alpine', None) # detached container, with tty ssh
    alpidetachedtty.run(['--detach', '-t'])
    containers.append(alpidetachedtty)

    # centos is a Linux distribution based on RedHat
    centosdetached = Container('centosdetached', 'centos', '/bin/bash') # detached container, running bash
    centosdetached.run(['--detach'])
    containers.append(centosdetached)

    # hello-world is a docker image that just prints hello world
    hw = Container('hw', 'hello-world', None) # simple container, runs 'hello-world'
    hw.run([])
    containers.append(hw)

    # nginx is a reverse proxy server
    nginxdetached = Container('nginx', 'nginx', None) # opens a proxy
    nginxdetached.run(['--detach'])
    containers.append(nginxdetached)

    # splunk is a fully functional splunk setup (with a web server)
    splunkdetached = Container('splunk', 'splunk/splunk', None) # starts a web server
    splunkdetached.run(['--detach', '-e', 'SPLUNK_START_ARGS=--accept-license', '-e', 'SPLUNK_PASSWORD=changeme'])
    containers.append(splunkdetached)

    Container.list_all()
    time.sleep(20)
    
    return containers
  
def part1(containers):
    for container in containers:
	    container.stop()

    Container.list_all()
    time.sleep(20)

    for container in containers:
	    container.start()

    Container.list_all()
    time.sleep(20)

def part2(containers):  
    pass

def main():
    containers = []

    containers = setup_containers()

    # Part 1. Testing what docker containers can be 'revived' through starting them after they are stopped
    part1(containers)

    # Part 2. Testing the trade off between security and time for the docker networking options
    part2(containers)

    # stop and remove all containers
    for container in containers:
        container.stop()
        container.remove()
	
main()
