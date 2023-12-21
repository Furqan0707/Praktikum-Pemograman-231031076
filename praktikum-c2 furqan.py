print("Nama : M Furqan Ramadhanu")
print("Nim  : 231031076")
print("Prodi: Sistem Informasi")
print("Tanggal Lahir : 10-10-2004")

#Operator Penugasan
print()
a = 76
print("Nilai a =", a)

print()
a+=2
print("Nilai a+=2 =", a)

print()
a-=2
print("Nilai a-=2 =", a)

print()
a*=2
print("Nilai a*=2 =", a)

print()
a/=2
print("Nilai a/=2 =", a)

print()
a%=2
print("Nilai a%=2 =", a)

print()
a**=2
print("Nilai a**=2 =", a)

print()
a//=2
print("Nilai a//=2 =", a)

print()
a = 76
a&=2
print("Nilai a&=2 =", a)

print()
a|=2
print("Nilai a|=2 =", a)

print()
a^=2
print("Nilai a^=2 =", a)

print()
a>>=2
print("Nilai a>>=2 =", a)

print()
a<<=2
print("Nilai a<<=2 =", a)

#Or
print()
b = True
print("Nilai b =",b)

b|=False
print("Nilai b|=False akan menjadi",b)

b=False
print("Nilai b=False akan menjadi",b)

b|=False
print("Nilai b|=False akan menjadi",b)

#AND
b=True
print("Nilai b =",b)

b&=False
print("Nilai b|=False akan menjadi",b)

b=False
print("Nilai b =",b)

b&=False
print("Nilai b|=False akan menjadi",b)

#XOR
b=True
print("Nilai b =",b)

b^=False
print("Nilai b|=False akan menjadi",b)

b=False
print("Nilai b =",b)

b^=False
print("Nilai b|=False akan menjadi",b)

#Shifthing
c=0b0100
print("Nilai c =",format(c, "04b"))

c>>=1
print("Nilai c>>=1 akan menjadi",format(c, "04b"))

c<<=1
print("Nilai c<<=1 akan menjadi",format(c, "04b"))

#Operasi Komparasi/Perbandingan
a=6
b=7
print("================== Besar dari 11")
hasil = a>6
print(a,"> 6 adalah",hasil)
hasil = b>11
print(b,"> 11 adalah",hasil)

print("================== Kecil dari 11")
hasil = a<6
print(a,"< 6 adalah",hasil)
hasil = b<=11
print(b,"< 11 adalah",hasil)

print("================== Besar atau sama dari 11")
hasil = a>=6
print(a,">= 6 adalah",hasil)
hasil = b>=11
print(b,">= 11 adalah",hasil)

print("================== Kecil atau sama dari 11")
hasil = a<=6
print(a,"<= 6 adalah",hasil)
hasil = b<=11
print(b,"<= 11 adalah",hasil)

print("================== Sama dengan 11")
hasil = a==11
print(a,"== 11 adalah",hasil)
hasil = b==11
print(b,"== 11 adalah",hasil)

print("================== Tidak sama dengan 11")
hasil = a!=6
print(a,"!= 6 adalah",hasil)
hasil = b!=11
print(b,"!= 11 adalah",hasil)

#Operasi Logika
print("=============NOT=============")
a=Truec = not a
print("a adalah",a)
print("------c = not a-------NOT")
print("c adalah",c)

print("=============OR=============")
a=True
b=True
c=a or b
print(a, "OR",b,"menjadia",c)

a=True
b=False
c=a or b
print(a, "OR",b,"menjadia",c)

a=False
b=True
c=a or b
print(a, "OR",b,"menjadia",c)

a=False
b=False
c=a or b
print(a, "OR",b,"menjadia",c)

print("=============AND=============")
a=True
b=True
c=a or b
print(a, "AND",b,"menjadia",c)

a=True
b=False
c=a or b
print(a, "AND",b,"menjadia",c)

a=False
b=True
c=a or b
print(a, "AND",b,"menjadia",c)

a=False
b=False
c=a or b
print(a, "AND",b,"menjadia",c)

print("=============XOR=============")
a=True
b=True
c=a ^ b
print(a, "^",b,"menjadia",c)

a=True
b=False
c=a ^ b
print(a, "^",b,"menjadia",c)

a=False
b=True
c=a ^ b
print(a, "^",b,"menjadia",c)

a=False
b=False
c=a ^ b
print(a, "^",b,"menjadia",c)

#TUGAS
#Buat kode untuk masing masing operator berikut
print("=============NAND=============")
print("=============NOR=============")
print("=============NXOR=============")

#jawaban
print("=============NAND=============")
hasil = not(a and a)
print(a, "nand", b, "adalah =",hasil)
hasil = not(a and b)
print(a, "nand", b, "adalah =",hasil)
hasil = not(b and a)
print(b, "nand", b, "adalah =",hasil)
hasil = not(b and b)
print(b, "nand", b, "adalah =",hasil)
print()
print("=============NOR=============")
hasil = not(a or a)
print(a, "nor", a, "adalah =",hasil)
hasil = not(a or b)
print(a, "nor", b, "adalah =",hasil)
hasil = not(b or a)
print(a, "nor", b, "adalah =",hasil)
hasil = not(b or b)
print(a, "nor", b, "adalah =",hasil)
print()
print("=============NXOR=============")
hasil = not(a ^ a)
print(a, "nxor", a, "adalah =",hasil)
hasil = not(a ^ b)
print(a, "nxor", b, "adalah =",hasil)
hasil = not(b ^ a)
print(b, "nxor", a, "adalah =",hasil)
hasil = not(b ^ b)
print(b, "nxor", b, "adalah =",hasil)
print()
print()
print()

#Operator Membership
print("======================= IN")
nama_lengkap = "Bachruddin Jusuf Habibie"
test = "a"
cek = test in nama_lengkap
print(test," terdapat di ",nama_lengkap," adalah ",str(cek))

test = "rud"
cek = test in nama_lengkap
print(test," terdapat di ",nama_lengkap," adalah ",str(cek))

test = "bac"
cek = test in nama_lengkap
print(test," terdapat di ",nama_lengkap," adalah ",str(cek))

print("=======================NOT IN")
nama_lengkap = "Bachruddin Jusuf Habibie"
test = "a"
cek = test not in nama_lengkap
print(test,"tidak terdapat di ",nama_lengkap," adalah ",str(cek))

test = "rud"
cek = test not in nama_lengkap
print(test,"tidak terdapat di ",nama_lengkap," adalah ",str(cek))

test = "bac"
cek = test not in nama_lengkap
print(test,"tidak terdapat di ",nama_lengkap," adalah ",str(cek))

#Tugas
#Dengan cara yang sama buat operator in dan not in , ubah nama ←- lengkap menjadi nama masing - masing dengan uji test
test1 = "fu"
test2 = "uf"
test3 = "a"
test4 = "i"
test5 = "e"
test6 = "o"

#Operator Bitwise
a=10
a +=60
b=10
b+= 90
print("=============================OR")
print("Nilai",a,"dalam biner    =", format(a,"08b"))
print("Nilai",b,"dalam biner    =", format(b,"08b"))
print( "----------------------------(|)")
hasil=a|b
print("Nilai",a,"|",b,"dalam biner =", format(hasil,"08b"))

print("=============================AND")
print("Nilai",a,"dalam biner    =", format(a,"08b"))
print("Nilai",b,"dalam biner    =", format(b,"08b"))
print( "----------------------------(&)")
hasil=a&b
print("Nilai",a,"&",b,"dalam biner =", format(hasil,"08b"))

print("=============================XOR")
print("Nilai",a,"dalam biner    =", format(a,"08b"))
print("Nilai",b,"dalam biner    =", format(b,"08b"))
print( "----------------------------(^)")
hasil=a^b
print("Nilai",a,"^",b,"dalam biner =", format(hasil,"08b"))

print("=============================NOT")
print("Nilai",a,"dalam biner    =", format(a,"08b"))
print("Nilai",b,"dalam biner    =", format(b,"08b"))
print( "----------------------------(~a)")
hasil= ~a
print("Nilai ~",a,"dalam biner =", format(hasil,"08b"))

print("Nilai",a,"dalam biner    =", format(a,"08b"))
print("Nilai",b,"dalam biner    =", format(b,"08b"))
print( "----------------------------(~b)")
hasil= ~b
print("Nilai ~",b,"dalam biner =", format(hasil,"08b"))

print("=============================>>")
print("Nilai",a,"dalam biner    =", format(a,"08b"))
print("Nilai",b,"dalam biner    =", format(b,"08b"))
print( "----------------------------(>>2)")
hasil= a >> 2
print("Nilai ~",a,"dalam biner =", format(hasil,"08b"))

print("Nilai",a,"dalam biner    =", format(a,"08b"))
print("Nilai",b,"dalam biner    =", format(b,"08b"))
print( "----------------------------(<<2)")
hasil= b << 2
print("Nilai ~",b,"dalam biner =", format(hasil,"08b"))
print()
# TUGAS
text = '============================= NOT AND'

# Membuat list dari representasi ASCII setiap karakter dalam teks
ascii_values = [ord(char) for char in text]

# Membuat representasi biner dari setiap nilai ASCII
binary_values = [bin(value)[2:].zfill(8) for value in ascii_values]

# Menggabungkan representasi biner menjadi satu string
binary_string = ''.join(binary_values)

print(binary_string)

print()
text = ' ============================= NOT OR '

binary_values = [bin(ord(char))[2:].zfill(8) for char in text]
binary_string = ''.join(binary_values)

print(binary_string)
print()
text = ' ============================= NOT XOR '

binary_values = [bin(ord(char))[2:].zfill(8) for char in text]
binary_string = ''.join(binary_values)

print(binary_string)
print()
text = ' ============================= NOT ( > >2) '

binary_values = [bin(ord(char))[2:].zfill(8) for char in text]
binary_string = ''.join(binary_values)

print(binary_string)
print()
text = ' ============================= NOT ( < <2) '

binary_values = [bin(ord(char))[2:].zfill(8) for char in text]
binary_string = ''.join(binary_values)

print(binary_string)



