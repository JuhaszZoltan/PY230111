from random import randint

szamok:list[int] = []
for i in range(200):
    szamok.append(randint(11, 99))

for index in range(len(szamok)):
    print(szamok[index], end=' ')
    if (index + 1) % 25 == 0:
        print()

osszeg:int = 0
for szam in szamok:
    osszeg += szam
print(f'számok átlaga: {osszeg / len(szamok)}')