from time import sleep
from os import system

szoveg:str = input('írj be valamit: ')

for i in range(len(szoveg)):
    system('cls')
    print(i * ' ', end='')
    print(szoveg[i])
    sleep(.25)
system('cls')
print(szoveg)