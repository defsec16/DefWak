import os
os.system('clear')
bannerD = '''
		88888888ba,              88888888ba,    88888888ba,      ,ad8888ba,     ad88888ba   
		88      `"8b             88      `"8b   88      `"8b    d8"'    `"8b   d8"     "8b  
		88        `8b            88        `8b  88        `8b  d8'        `8b  Y8,          
		88         88            88         88  88         88  88          88  `Y8aaaaa,    
		88         88  aaaaaaaa  88         88  88         88  88          88    `"""""8b,  
		88         8P  """"""""  88         8P  88         8P  Y8,        ,8P          `8b  
		88      .a8P             88      .a8P   88      .a8P    Y8a.    .a8P   Y8a     a8P  
		88888888Y"'              88888888Y"'    88888888Y"'      `"Y8888Y"'     "Y88888P"   
											~Code by Alisher	    '''

print(bannerD)
text = '''                
		       --{Menu}-
		       --{Меню}--
		[1]-DDOS (version 1)
		[2]-DDOS (version 2)
		[3]-DDos-Attack-OVH (Coded by HardyTomas)
		
		[99]-назад в меню(back to main manu)
		[0]-Выйти из программы(Exit the program)
			'''
print(text)
d = int(input('D-ddos~#:'))  
def ddosv1():
	os.system('python Dddos.py')
def ddosv2():
	os.system('python ddos-attack.py')
def ddosv3():
	text = """
	Теперь пишем на каком порту сайт
Если 80:
python3 80port.py
Если 443:
python3 443port.py
--------------------------------------------------------------
У нас открылась утилита
Insert URL/IP:Вводим сайт
--------------------------------------------------------------
Do you want to perform HTTP/S flood '0'(best), TCP flood '1' or UDP flood '2' ? :
Пишем 0
--------------------------------------------------------------
Do you want proxy/socks mode? Answer 'y' to enable it: Здесь пишем хотим ли мы испозьзовать proxy.txt или socks.txt
--------------------------------------------------------------
Пишем повторения атаки
--------------------------------------------------------------
Потои пишем мощность
Если у вас слабый интернет или слабый телефон лучше не указывать большое число
--------------------------------------------------------------
Жмём Enter (Ввод) и у нас запускается атака """
	os.chdir("HardyTomas")
def ddosExit():
	print('Прощайте!(Goodbye!)')
	raise SystemExit
def ddosExit99():
	os.system('python defwak.py')

if d ==1:
	ddosv1()
elif d ==2:
	ddosv2()
elif d ==3:
	ddosv3()
elif d ==99:
	ddosExit99() 
elif d ==0:
	ddosExit()
else:
	print('Ошибка:не найдено(Error:not found)')
