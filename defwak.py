#code written and owned by DefSec16 or Alisher Zhussip
import os, random, time
os.system("clear")
ban = random.randint(0,2)
if ban ==0:
  banner =''' \u001b[32m"
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
  banner = ''' 
                                                                                          
        88888888ba,                   ad88  I8,        8        ,8I            88         
        88      `"8b                 d8"    `8b       d8b       d8'            88         
        88        `8b                88      "8,     ,8"8,     ,8"             88         
        88         88   ,adPPYba,  MM88MMM    Y8     8P Y8     8P  ,adPPYYba,  88   ,d8   
        88         88  a8P_____88    88       `8b   d8' `8b   d8'  ""     `Y8  88 ,a8"    
        88         8P  8PP"""""""    88        `8a a8'   `8a a8'   ,adPPPPP88  8888[      
        88      .a8P   "8b,   ,aa    88         `8a8'     `8a8'    88,    ,88  88`"Yba,   
        88888888Y"'     `"Ybbd8"'    88          `8'       `8'     `"8bbdP"Y8  88   `Y8a       '''
else:
  banner = ''' \u001b[32m"
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
	  -{Main Menu}-
         -{Главное Меню}-
      Что вам будет угодно?(what do you want?)
        [1]-DSpamers
        [2]-D-ddos
        [3]-passgen
	[4]-backdoor[Скоро]
	[5]-SkanNet
	[6]-В плане
	[7]-В плане
	
	[99]-Информация(Information)
	[0]-Выход(exit)
        (select number)Выберите номер:
        '''
print(text)
a = int(input("DefWak~#:"))

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
	os.system("clear")
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
	             -{Menu}-
		    --{Меню}--
	     [1]-backdoor{server} (Создать)(Create)
	     [2]-backdoor{client} (Создать)(Create)
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
		print("Скоро(soon)")
		time.sleep(5)
		DefSec4()
	def Backdoor2():
		print("Скоро(soon)")
		time.sleep(5)
		DefSec4()
	def Backdeoo3():
		print("Скоро(soon)")
		time.sleep(5)
		DefSec4()
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
	text = """
	Информация о программах:
	1)DSpamers - DefineSpamers = Определить спамер
	на данный момент есть 3 версии спамеров
	2)D-DDos - DefineDDos = Определить ДДосер
	на данный момент есть 3 разных ддосреа
	3)PassGen - Password Generation - Генерация пароля по ключевым словам
	Оно генерирует пароли по словам чем больше слов список паролей сохраняется в txt формате
	4)BackDoor - Черный вход 
	Нужен для удаленного контроля при помощи терминала состоит из клиента который должен запустить мамонт(Жертва)
	и сервера который должен запустить хакер 
	5)SkanNet -Skaner Network = Сконирование сети
	Сканирует и отправляет пакеты на запрос МАК Адреса
	нужно быть в одной сети работает на Linux
	"""
	print(text)
def DefSec5():
	os.chdir("SkanNet")
	os.system("python3 skannet.py")
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
else ValueError:
	print('Ошибка:не найдено(Error:not found)')
