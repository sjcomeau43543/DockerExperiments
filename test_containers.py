from Container import Container
import time
  
def main():
	part1 = 0
	part2 = 1

	containers = []

	# create some containers with differing attributes

	# alpine is a Linux distribution based on busybox
	alpi = Container('alpi', 'alpine', None) # stripped container, no options
	alpi.run([])
	containers.append(alpi)

	alpidetached = Container('alpidetached', 'alpine', None) # detached container, no program
	alpidetached.run(['--detach'])
	containers.append(alpidetached)

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

	
	# Part 1. Testing what docker containers can be 'revived' through starting them after they are stopped
	if part1:
		for container in containers:
			container.stop()

		Container.list_all()
		time.sleep(20)

		for container in containers:
			container.start()

		Container.list_all()
		time.sleep(20)
	
	# Part 2. Testing what attributes make docker containers take so long to 'stop'
	if part2:
		hypothesis1 = 0
		hypothesis2 = 0

		# hypothesis1: the longer they are running the longer it will take to stop
		if hypothesis1:
			time.sleep(60)
		
		# hypothesis2: the more complex they are (ex opening port, setting credentials) the longer it will take to stop

		# generic
		for container in containers:
			container.time_stop()

		Container.list_all()
		time.sleep(20)

		for container in containers:
			container.logs(10)


	# stop and remove all containers
	for container in containers:
		container.stop()
		container.remove()
	
main()
