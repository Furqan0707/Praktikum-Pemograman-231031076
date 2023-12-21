import os
import random as rd
os.system('clear')

kesempatan = 3
com = rd.randint(1, 10)

print("Ayo tebak angka yang dipilih oleh komputer (1-10)!")

while kesempatan > 0:
    tebakan = int(input("Tebak angka: "))
    
    if tebakan == com:
        print("Selamat, tebakanmu benar!")
        break
    else:
        kesempatan -= 1
        if kesempatan > 0:
            print(f"Kesempatan Anda tersisa {kesempatan} kali.")
        else:
            print(f"Maaf, angka yang dipilih oleh komputer adalah {com}. Kamu kalah!")