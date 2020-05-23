import os
os.system("Clear")
banner ='''\u001b[32m"
		                                                                                             
		 ad88888ba                                                                                   
		d8"     "8b                                                                                  
		Y8,                                                                                          
		`Y8aaaaa,    8b,dPPYba,   ,adPPYYba,  88,dPYba,,adPYba,    ,adPPYba,  8b,dPPYba,  ,adPPYba,  
		  `"""""8b,  88P'    "8a  ""     `Y8  88P'   "88"    "8a  a8P_____88  88P'   "Y8  I8[    ""  
		        `8b  88       d8  ,adPPPPP88  88      88      88  8PP"""""""  88           `"Y8ba,   
		Y8a     a8P  88b,   ,a8"  88,    ,88  88      88      88  "8b,   ,aa  88          aa    ]8I  
		 "Y88888P"   88`YbbdP"'   `"8bbdP"Y8  88      88      88   `"Ybbd8"'  88          `"YbbdP"'  
		             88                                                                              
		             88                                                                              
		             '''
print(banner)             
text = '''	  -{Menu}-
	  -{Меню}-
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
	os.system('python DW.py')
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

