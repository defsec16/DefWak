import os, random
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
text = ''' 	-{Menu}-
	    --{Меню}--
     [1]-backdoor{server} (Создать)(Create)
     [2]-backdoor{client} (Создать)(Create)
     [3]-Применение(application)

     [99]-Назад в главное меню(back to main menu)
     [0]-Выход(Exit)
     '''
print(text)
back = int(input("Backdoor~#"))
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
	os.system("python DW.py")
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
