#code written and owned by DefSec16 tobish Alisher Zhussip
import os, random
os.system("clear")
ban = random.randint(0,2)
if ban ==0:
  banner ='''
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
text ='''          -{Main Manu}-
         -{Главное Меню}-
      Что вам будет угодно?(what do you want?)
        [1]-DSpamers
        [2]-D-ddos
        [3]-passgen
	[4]-backdoor[Скоро]
	
	[0]-Выход(exit)
        (select number)Выберите номер:
        '''
print(text)
a = int(input("DefWak~#:"))

def DefSec0():
	print("Прощайте!(Goodbye!)")
	raise SystemExit
def DefSec1():
  	import os
  	os.system("Clear")
	banner ='''\u001b[32m"
		 _____                                     
		/  ___|                                    
		\ `--. _ __   __ _ _ __ ___   ___ _ __ ___ 
		 `--. \ '_ \ / _` | '_ ` _ \ / _ \ '__/ __|
		/\__/ / |_) | (_| | | | | | |  __/ |  \__ \
		\____/| .__/ \__,_|_| |_| |_|\___|_|  |___/
		      | |                                  
		      |_|                                                                                                          
				     '''
	print(banner)             
	text = '''	  
		  -{Menu}-
		 --{Меню}--
	      [1]-DSpamer(Version 1)
	      [2]-DSpamer(Version 2)
	      [3]-DSpamer(Version 3)

	      [99]-Назад в главное меню(back to main menu)
	      [0]-Выйти из программы(Exit the program)
	      '''
	print(text)
	sp =int(input("Spamers~#:"))   

	def DSV1():
		import os
		os.system('python DSpamer.py')
	def DSV2():
		import os
		os.system("python DSpamerV2.py")
	def DSV3():
		import os
		os.system('python DSpamerV3open.py')
	def DS99():
		import os 
		os.system('python defwak.py')
	def DS0():
		print('Прощайте!(Goodbye!)')
		raise SystemExit 

	if sp ==1:
		DSV1()
	elif sp ==2:
		DSV2()
	elif sp ==3:
		DSV3()
	elif sp ==0:
		DS0()
	elif sp ==99:
		DS99()
	else:
		print('Ошибка:не найдено(Error:not found)')
def DefSec2():
  	import os
  	os.system('clear')

	banner = '''
		88888888ba,              88888888ba,    88888888ba,      ,ad8888ba,     ad88888ba   
		88      `"8b             88      `"8b   88      `"8b    d8"'    `"8b   d8"     "8b  
		88        `8b            88        `8b  88        `8b  d8'        `8b  Y8,          
		88         88            88         88  88         88  88          88  `Y8aaaaa,    
		88         88  aaaaaaaa  88         88  88         88  88          88    `"""""8b,  
		88         8P  """"""""  88         8P  88         8P  Y8,        ,8P          `8b  
		88      .a8P             88      .a8P   88      .a8P    Y8a.    .a8P   Y8a     a8P  
		88888888Y"'              88888888Y"'    88888888Y"'      `"Y8888Y"'     "Y88888P"   
												    '''

	print(banner)
	text = '''                
			-{Menu}-
		       --{Меню}--
		[1]-DDOS (version 1)
		[2]=DDOS (version 2)
		[99]-назад в меню(back to main manu)
		[0]-Выйти из программы(Exit the program)
			'''
	print(text)
	d = int(input('D-ddos~#:'))  

	def ddosv1():
		import os
		os.system('python Dddos.py')
	def ddosv2():
		import os
		os.system('python ddos-attack.py')    
	def ddosExit():
		print('Прощайте!(Goodbye!)')
		raise SystemExit
	def ddosExit99():
		import os
		os.system('python defwak.py')

	if d ==1:
		ddosv1()
	elif d ==2:
		ddosv2()
	elif d ==99:
		ddosExit99() 
	elif d ==0:
		ddosExit()
	else:
		print('Ошибка:не найдено(Error:not found)')
def DefSec3():
  import os
  os.system('python passgen.py')
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
		print("Прощайте!(Goodbyr!)")
		raise SystemExit
	def Backdoor1():
		print("Скоро(soon)")
	def Backdoor2():
		print("Скоро(soon)")
	def Backdeoo3():
		print("Скоро(soon)")
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

else:
  print('Ошибка:не найдено(Error:not found)')
