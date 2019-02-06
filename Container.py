import subprocess, time
import numpy as np

def call_subp(cmd):
	print 'Calling: ', cmd
	subp = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
	subp.wait()
	out, _ = subp.communicate()

	print 'Output: ', out


class Container:
	name = None
	service = None
	program = None
	network = None
	run_time_average = None
	start_time_average = None
	stop_time_average = None
	run_times = np.array([])
	start_times = np.array([])
	stop_times = np.array([])

	def __init__(self, name, service, program, network_name):
		self.name = name
		self.service = service
		if program is not None:
			self.program = program
		if network_name is not None:
			self.network = network_name
			self.name = name+'_'+str(network_name)

	def run(self, options):
		cmd = ['sudo', 'docker', 'run', '--name', self.name]
	
		for option in options:
			cmd.append(option)

		if self.network is not None:
			cmd.append('--net='+str(self.network))
	
		cmd.append(self.service)
	
		if self.program is not None:
			cmd.append(self.program)

		start = time.time()
		call_subp(cmd)
		self.run_times = np.append(self.run_times, [time.time() - start])


	def stop(self):
		cmd = ['sudo', 'docker', 'stop', self.name]
		start = time.time()
		call_subp(cmd)
		self.stop_times = np.append(self.stop_times, [time.time() - start])

	def start(self):
		cmd = ['sudo', 'docker', 'start', self.name]
		start = time.time()
		call_subp(cmd)
		self.start_times = np.append(self.start_times, [time.time() - start])

	def calculate_averages(self):
		print 'Averaging...'
		self.run_time_average = np.average(self.run_times)
		self.start_time_average = np.average(self.start_times)
		self.stop_time_average = np.average(self.stop_times)
		print str(self.run_times), ':average:', self.run_time_average
		print str(self.start_times), ':average:', self.start_time_average
		print str(self.stop_times), ':average:', self.stop_time_average

	def remove(self):
		cmd = ['sudo', 'docker', 'rm', self.name]
		call_subp(cmd)

	def logs(self, number):
		cmd = ['sudo', 'docker', 'logs', '--tail='+str(number), '--details', '-t', self.name]
		call_subp(cmd)

	@staticmethod
	def list_all():
		cmd = ['sudo', 'docker', 'container', 'ls', '--all']
		call_subp(cmd)

	@staticmethod
	def create_private_network(network_name):
		cmd = ['sudo', 'docker', 'network', 'create', '--driver', 'bridge', network_name]
		call_subp(cmd)

	@staticmethod
	def inspect_network(network_name):
		if network_name is None:
			network_name = 'bridge' # default network name
		cmd = ['sudo', 'docker', 'network', 'inspect', network_name]
		call_subp(cmd)

	@staticmethod
	def remove_network(network_name):
		cmd = ['sudo', 'docker', 'network', 'rm', network_name]
		call_subp(cmd)
		
		
		

	
