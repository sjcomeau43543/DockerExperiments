from Container import Container
  
def main():
	alpi = Container('alpi', 'alpine')
	alpi.run([])

	alpidetached = Container('alpidetached', 'alpine')
	alpidetached.run(['--detach'])

	alpidecentosdetachedtached = Container('centosdetached', 'centos')
	centosdetached.run(['--detach'])

	alpi.stop()
	alpidetached.stop()
	centosdetached.stop()
  
main()
