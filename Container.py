import subprocess

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

	def __init__(self, name, service, program):
		self.name = name
		self.service = service
		if program is not None:
			self.program = program

	def run(self, options):
		cmd = ['sudo', 'docker', 'run', '--name', self.name]
		for option in options:
			cmd.append(option)
		cmd.append(self.service)
		if self.program is not None:
			cmd.append(self.program)

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
		
		

	
