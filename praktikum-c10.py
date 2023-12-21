import os


def judul():
    os.system('cls')
    print('PROGRAM MENGHITUNG VOLUME DAN LUAS PERMUKAAN')
    print('BANGUN RUANG BALOK')
    print()

def inputan():
        p = float(input('Masukan Panjang: '))
        l = float(input('Masukkan lebar: '))
        t = float(input('Masukan Tinggi'))
        return p,l,t

def perhitungan(p,l,t):
    vol = p * l * t
    luas = 2 * (p*l  + p*t + l*t)
    luas_non_tutup = luas - p*l
    return vol,luas,luas_non_tutup

def tampilkan(jenis,nilai):
    print(f'Nilai dari {jenis} adalah : {nilai}')

def pilihan():
    pilih = input('Apakah lanjutkan? [y/n]')
    if pilih == 'y' :
        a = True
    else:
        a = False
        print('Sampai jumpa lagi.')
        return a
def main():
     judul()

a = True
while a:
    # judul
    judul()



    # inputan
    p,l,t = inputan()

    # perhitungan
    vol,luas,luas_non_tutup = perhitungan(p,l,t)

    # tampilkan
    tampilkan('volume',vol)
    tampilkan('luas permukaan',vol)
    tampilkan('luas permukaan tanpa tutup',luas_non_tutup)

    #pilihan 
    a = pilihan()           # pilihan


    a = True
    while a:
         main()
    