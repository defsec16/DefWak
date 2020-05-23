#code written and owned by DefSec16 tobish Alisher Zhussip
import os, random
os.system("Clear")
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
text =''' -{Main Manu}-
         -{Главное Меню}-
      Что вам будет угодно?(what do you want?)
        [1]-DSpamers
        [2]-D-ddos
        [3]-passgen
        [4]-recreator-phishing
	[5]-backdoor[Скоро]

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
  os.system('python Spamers.py')
def DefSec2():
  import os
  os.system('python D-DDOS.py')
def DefSec3():
  import os
  os.system('python passgen.py')
def DefSec4():
  import os
  os.system("python recreator-phishing.py")
def DefSec5():
	os.system("python backdoor.py")

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
else:
  print('Ошибка:не найдено(Error:not found)')
