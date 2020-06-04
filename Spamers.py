import os
os.system("сlear")

banner = '''
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
  os.system("python DSpamer.py")
def DSV2():
  os.system("python DSpamerV2.py")
def DSV3():
  os.system('python DSpamerV3open.py')
def DS99(): 
  os.system('python defwak.py')
def DS0():
  print('Прощайте!(Goodbye!)')
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
	print('Ошибка:не найдено(Error:not found)')
