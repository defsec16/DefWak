import os
from time import sleep
def clean():
  try:
    os.system('clear')
  except:
    os.system('cls')
clean()
banner = """                                                                                                             
                                                                 
                                      \033[31m                                          
                                       .,,,,,,,,,,,.                                            
                                    .',:odddodddoolc;'.                                         
                                 .'cllllloollodoooooolc:;.                                      
                               .':llllclc:clcloolccloolcc:'.                                    
                              ';:llc::ccc::c:collc:cl:;;:cc:'.                                  
                             ;lccclc;;;;;::c::cccclllcclolool,.                                 
                            'looc;,'....'cc;..';cll;'''';coool,                                 
                           .:lol,.      .;c.   .c;..     .'ldo:.                                
                           .:c:'         .:'   .;,         'llc;.                               
                           ,::;.      ...;'     .c;.       .:cl;.                               
                          .':c:.   ..';;,'.      ;ol;'.''. .:loc.                               
                          .,;:c;,,;:llc:;.. .... ,looolooc::cccc,                               
                         .'::::cc::ccc:cc:;;ccc::clooooodoooc::c:.                              
                         .';;,',,.':cccccccccclllllooodl;,;;,',lc.                              
                          .;;,..   .;llc::c:cllllllllo:.    .,cl;.                              
                          .;;:c:,.  .cc:,;c::clccccool'  .;:;cc:'                               
                          ..,;cc;.  ;oc;,;:;;cl:;:lolo:...cccc;.                                
                            .;:ccc,.coc:'.....'...'lolc..;c;;c;.                                
                            .',::c;';c;..          .'::'.:l:::,.                                
                              .;c:. ..               .. .co:...                                 
                               ,c;.                     .co:.                                   
                              '::;'.                   .;ool,.                                  
                              .;:::,                   ,lool,                                   
                               ,llll;..             ..;looo:.                                   
                               .;loool;.           .,cllll:.                                    
                                 ,llloc;,..',,''...,c::cc,.                                     
                                  .:clllllllllollcclllc;'                                       
                                   .'coooolclc:cllcoo:..                                        
                                     .;lollool:cllloc'                                          
                                      .,looooolllloc.                                           
                                       .:oooooooll;.                                            
                                        ..........          
                                   """        
print(banner)
sleep(2)
print('\033[32m')
os.system('python zagruzka.py')
os.system('python defwak.py')
