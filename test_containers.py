import subprocess

def create_container(service, options):
  cmd = ['sudo', 'docker', 'run']
  for option in options:
    cmd.append(option)
  cmd.append(service)
  
  print 'Calling: ', cmd 
  subp = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
  subp.wait()
  out, _ = subp.communicate()
  
  print 'Output: ', out
  print '------'
  
def modify_container(command, name):
  cmd = ['sudo', 'docker', command, name]
 
  print 'Calling: ', cmd 
  subp = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
  subp.wait()
  out, _ = subp.communicate()
  
  print 'Output: ', out
  print '------'
  
def main():
  create_container('alpine', ['--name', 'alpi'])
  create_container('alpine', ['--detach', '--name', 'alpidetached')
  create_container('centos', ['--detach', '--name', 'centosdetached'])
  
  
  #modify_container('stop', 'alpi')
  #modify_container('rm', 'alpi')
  #modify_container('stop', 'alpidetached')
  #modify_container('rm', 'alpidetached')
  #modify_container('stop', 'centosdetached')
  #modify_container('rm', 'centosdetached')
  
main()