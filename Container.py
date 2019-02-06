import subprocess, time

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
	run_time = None
	start_time = None
	stop_time = None

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
		self.run_time = time.time() - start


	def stop(self):
		cmd = ['sudo', 'docker', 'stop', self.name]
		start = time.time()
		call_subp(cmd)
		self.stop_time = time.time() - start

	def start(self):
		cmd = ['sudo', 'docker', 'start', self.name]
		start = time.time()
		call_subp(cmd)
		self.start_time = time.time() - start

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
		
		
		

	
