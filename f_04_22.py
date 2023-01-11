szoveg:str = input('írj be egy szöveget: ')
karakterek:list[chr] = []

for k in szoveg:
    if k not in karakterek:
        karakterek.append(k)

print(karakterek)
print(f'különböző karakterek száma: {len(karakterek)}')