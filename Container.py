def call_subp(cmd):
	print 'Calling: ', cmd
	subp = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
	subp.wait()
	out, _ = subp.communicate()

	print 'Output: ', out

class Container:
    name = ''
	service = ''
	program = ''
	

	def __init__(self, name, service):
    	self.name = name
		self.service = service

	def __init__(self, name, service, program):
    	self.name = name
		self.service = service
		self.program = program

	def run(self, options):
		cmd = ['sudo', 'docker', 'run', '--name', self.name]
		for option in options:
			cmd.append(option)
		cmd.append(self.service)

		call_subp(cmd)
		

	def stop(self):
		cmd = ['sudo', 'docker', 'stop', self.name]
		call_subp(cmd)

	def time_stop(self):
		cmd = ['time', 'sudo', 'docker', 'stop', self.name]
		call_subp(cmd)

	def start(self):
		cmd = ['sudo', 'docker', 'start', self.name]
		call_subp(cmd)
		

	
