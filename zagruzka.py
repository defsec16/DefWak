import os,time
os.system('clear')
os.chdir('gif')
gif = ["1.txt","2.txt","3.txt","4.txt","5.txt","6.txt","7.txt","8.txt","9.txt","10.txt","11.txt","12.txt","13.txt","15.txt","16.txt","17.txt"]
def animator(gif,delay=1,repeat=10000):
  frames = []
  for wak in gif:
    with open(wak,"r",encoding="utf-8") as d:
      frames.append(d.readlines())
  for i in range(repeat):
    for frame in frames:
      print("".join(frame))
      time.sleep(delay)
      os.system('clear')
animator(gif,delay=0.1,repeat=5)
