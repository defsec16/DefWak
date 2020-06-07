import os
def clean():
	try:
		os.system('clear')
	except:
		os.system('cls')
clean()
banner = '''\033[32m
 _____                                     
/  ___|                                    
\ `--. _ __   __ _ _ __ ___   ___ _ __ ___ 
 `--. \ '_ \ / _` | '_ ` _ \ / _ \ '__/ __|
/\__/ / |_) | (_| | | | | | |  __/ |  \__ 
\
\____/| .__/ \__,_|_| |_| |_|\___|_|  |___/
      | |                                  
      |_|                                  
		'''

print(banner)
text = '''	\033[35m  
	    -{Menu}-
	   --{Меню}-- \033[34m
      [1]-DSpamer(Version 1)
      [2]-DSpamer(Version 2)
      [3]-DSpamer(Version 3)
      \033[36m
      [99]-Назад в главное меню(back to main menu)
      [0]-Выйти из программы(Exit the program)
      '''
print(text)
sp =int(input("\033[31mSpamers\033[37m~#:"))   
def DSV1():
  os.system("python DSpamer.py")
def DSV2():
  os.system("python DSpamerV2.py")
def DSV3():
  os.system('python DSpamerV3open.py')
def DS99(): 
  os.system('python defwak.py')
def DS0():
  print('\033[32mПрощайте!(Goodbye!)')
  raise SystemExit 
if sp == 1:
  DSV1()
elif sp == 2:
  DSV2()
elif sp == 3:
  DSV3()
elif sp == 0:
  DS0()
elif sp ==99:
  DS99()
else:
	print('\033[31mОшибка:не найдено(Error:not found)')
	time.sleep(2)
	os.system('python Spamers.py')
