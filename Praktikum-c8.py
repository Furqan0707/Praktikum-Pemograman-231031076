import os
import random as rd
os.system('clear')

warna = ('merah,putih,hitam')
com = rd.choice(warna)
a = True
while a:
    pilih = input('masukkan pilihan [merah,putih,htam]:\n')
    if pilih == com:
        print('pilihan anda benar yaitu {pilih} \n')
        a = False
    else:
        print('tebakan anda salah coba lagi.')
