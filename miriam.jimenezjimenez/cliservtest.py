import unittest

class cliservTest(unittest.TestCase):
	# Compueba que el servidor se conecta a un cliente
	def test_serv_conn():
		ss = socket.socket(socket.AF_INET, socket.SOCK_DGRAM,0)
		dir_socket = ('localhost', 16013)
		ss.bind(dir_socket)
		data, dirc = ss.recvfrom(1024)
		assert dirc is not None
		ss.close()
	
	#Compueba que el cliente se conecta al servidor
	def test_cli_conn():
		sc = socket.socket(socket.AF_INET, socket.SOCK_DGRAM,0)
		dir_socket = ('localhost', 16013)
		sc.sendto('conn test'.encode('utf8'), dir_socket)
		sc.close()
		

	
	
	
		
	
	if __name__ == '__main__':
		unittest.main()
