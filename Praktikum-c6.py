import os
os.system('clear')

a = True

while a:
    pilih = input('Apakah ingin melanjutkan?[y/n]')
    if pilih == 'y':
        print('Terima kasih!')
    elif pilih == 'n':
        print('Sampai jumpa lagi!)')
    else:
        print('Jangan aneh deh! :(')