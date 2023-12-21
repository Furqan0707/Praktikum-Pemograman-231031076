nama = 'm furqan ramadhanu'
nim = '231031076'
meet = 'praktikum 3 (string)'
prodi = 'Sistem Informasi'
email = '0707furqan@gmail.com'
kota = 'Sidenreng rappang'
lahir = '10-oktober-2004'
alamat = 'alamat desa belawae'
hobi = 'main volly'
tinggi = 163

sp=40
print('-'*sp)
print(nama.upper().center(sp))
print(nim.center(sp))
print('\n'*2)
print(meet.rjust(sp))
print(prodi.rjust(sp))
print(email.lower().rjust(sp))
print('-')

print(f'''   Halo,nama saya {nama} dengan NIM {nim} dari prodi {prodi} ini adalah file {meet},'terima kasih''')
print()
print(f'''Biodata saya,
      
Nama\t:{nama.upper()}
NIM\t:{nim}
Prodi\t{prodi}
TTL\t:{kota},{lahir}
Alamat\t:{alamat}
Asal\t:{kota}
Hobi\t:{hobi}
Tinggi\t:{tinggi}CM

''')

stat1 = 'duFort Frankel Sir Issac'
# Issac duFort Frankel Sir

stat2 = 'duFort Frankel Sir Issac'
# d F S Issac

stat3 = 'duFort Frankel Sir Issac'
# duFort F S I

stat4 = 'duFort Frankel Sir Issac'
# I duFort Frankel Sir

stat5 = 'duFort Frankel Sir Issac'
# Issac d F S

stat6 = 'duFort Frankel Sir Issac'
# ISSAC D F S

stat7 = '#duFort Frankel Sir Issac$'
# duFort Frankel Sir Issac

stat8 = '#duFort-Frankel-Sir-Issac$'
# duFort Frankel Sir Issac

stat9 = '#duFort@ ^Frankel* (Sir( (Issac$'
# duFort Frankel Sir Issac

stat10 = '#duFort@-^Frankel*-(Sir(-(Issac$'
# DUFORT FRANKEL SIR ISSAC

stat1 = 'duFort Frankel Sir Issac'
# Issac duFort Frankel Sir
print(stat1[19:],stat1[0:19])

stat2 = 'duFort Frankel Sir Issac'
# d F S Issac
print(stat2[0],stat2[7],stat2[15],stat2[19:])

stat3 = 'duFort Frankel Sir Issac'
# duFort F S I
print(stat3[0:7],stat3[7],stat3[15],stat3[19])

stat4 = 'duFort Frankel Sir Issac'
# I duFort Frankel Sir
print(stat4[19],stat4[0:18])

stat5 = 'duFort Frankel Sir Issac'
# Issac d F S
print(stat5[19:],stat5[0],stat5[7],stat5[15])

stat6 = 'duFort Frankel Sir Issac'.upper()
# ISSAC D F S
print(stat6[19:],stat6[0],stat6[7],stat6[15])

stat7 = '#duFort Frankel Sir Issac$'
# duFort Frankel Sir Issac
stat7 = stat7.strip("#$")
print(stat7)

stat8 = '#duFort-Frankel-Sir-Issac$'
# duFort Frankel Sir Issac
stat8 = stat8.strip("#$").replace("-"," ")
print(stat8)

stat9 = '#duFort@ ^Frankel* (Sir( (Issac$'
# duFort Frankel Sir Issac
import re
stat9 = re.findall(r'\w+', stat9)
hasil = ' '.join(stat9)
print(hasil)

stat10 = '#duFort@-^Frankel*-(Sir(-(Issac$'
# DUFORT FRANKEL SIR ISSAC
import re
stat10 = re.findall(r'\w+', stat10)
hasil = ' '.join(stat10.upper() for stat10 in stat10)
print(hasil)



print()