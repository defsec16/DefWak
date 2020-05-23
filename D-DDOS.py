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
text = '''      -{Menu}-
		-{Меню}-
	[1]-DDOS (version 1)
	[2]=DDOS (version 2)

	[99]-назад в меню(back to main manu)
	[0]-Выйти из программы(Exit the program)
		'''
print(text)
d = int(input('D-ddos~#'))  

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
	os.system('python DW.py')

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
