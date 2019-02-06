from Container import Container
import matplotlib.pyplot as plt
import numpy as np
import time

def cleanup_containers(containers):
    for container in containers:
        container.stop()
        container.remove()

def setup_containers(network_name):
    containers = []

    # create some containers with differing attributes

    # alpine is a Linux distribution based on busybox
    alpi = Container('alpi', 'alpine', None, network_name) # stripped container, no options
    alpi.run([])
    containers.append(alpi)

    alpidetached = Container('alpidetached', 'alpine', None, network_name) # detached container, no program
    alpidetached.run(['--detach'])
    containers.append(alpidetached)

    alpidetachedtty = Container('alpidetachedtty', 'alpine', None, network_name) # detached container, with tty ssh
    alpidetachedtty.run(['--detach', '-t'])
    containers.append(alpidetachedtty)

    # centos is a Linux distribution based on RedHat
    centosdetached = Container('centosdetached', 'centos', '/bin/bash', network_name) # detached container, running bash
    centosdetached.run(['--detach'])
    containers.append(centosdetached)

    # hello-world is a docker image that just prints hello world
    hw = Container('hw', 'hello-world', None, network_name) # simple container, runs 'hello-world'
    hw.run([])
    containers.append(hw)

    # nginx is a reverse proxy server
    nginxdetached = Container('nginx', 'nginx', None, network_name) # opens a proxy
    nginxdetached.run(['--detach'])
    containers.append(nginxdetached)

    # splunk is a fully functional splunk setup (with a web server)
    splunkdetached = Container('splunk', 'splunk/splunk', None, network_name) # starts a web server
    splunkdetached.run(['--detach', '-e', 'SPLUNK_START_ARGS=--accept-license', '-e', 'SPLUNK_PASSWORD=changeme'])
    containers.append(splunkdetached)

    Container.list_all()
    time.sleep(10)
    
    return containers
  
def part1():
    containers, _ = setup_containers(None)    

    for container in containers:
	    container.stop()

    Container.list_all()
    time.sleep(20)

    for container in containers:
	    container.start()

    Container.list_all()
    time.sleep(20)

    cleanup_containers(containers)

def part2():  
    #Container.create_private_network('isolated_nw')
    containers_default = setup_containers(None) # time how long the default network takes
    containers_private = setup_containers('isolated_nw') # time how long the private network takes

    Container.inspect_network(None)
    Container.inspect_network('isolated_nw')

    # stop and start each container so we can see how long it takes
    for container in containers_default:
        container.stop()
        container.start()
    for container in containers_private:
        container.stop()
        container.start()

    run_times = np.array([])
    stop_times = np.array([])
    start_times = np.array([])
    run_times_private = np.array([])
    stop_times_private = np.array([])
    start_times_private = np.array([])

    # put all the times in lists so we can plot them
    for container in containers_default:
        run_times = np.append(run_times, [container.run_time])
        stop_times = np.append(stop_times, [container.stop_time])
        start_times = np.append(start_times, [container.start_time])
    for container in containers_private:
        run_times_private = np.append(run_times_private, [container.run_time])
        stop_times_private = np.append(stop_times_private, [container.stop_time])
        start_times_private = np.append(start_times_private, [container.start_time])
    
    # plot using matplotlib
    plt.plot(run_times, color='darkblue', label='run time default network')
    plt.plot(stop_times, color='maroon', label='stop time default network')
    plt.plot(start_times, color='darkgreen', label='start time default network')
    plt.plot(run_times_private, color='slateblue', label='run time private network', linestyle='dashed')
    plt.plot(stop_times_private, color='lightcoral', label='stop time private network', linestyle='dashed')
    plt.plot(start_times_private, color='palegreen', label='start time private network', linestyle='dashed')
    
    plt.legend()
    plt.ylabel('Time(s)')
    plt.xlabel('Container')
    plt.xticks([0,1,2,3,4,5,6], ['a','b','c','d','e','f','g'])
    plt.title('Comparing container run/start/stop times based on the network they are attached to')
    plt.show()

    cleanup_containers(containers_default)
    cleanup_containers(containers_private)

def main():

    # Part 1. Testing what docker containers can be 'revived' through starting them after they are stopped
    # part1()

    # Part 2. Testing the trade off between security and time for the docker networking options
    part2()

	
main()
