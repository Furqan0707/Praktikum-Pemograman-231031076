import os
os.system('clear')

nim = ["2","3","1","0","3","1","0","7","6"]
# akses item
print(nim)

print(f'item indeks:0 (pertama) {nim[0]}')
print(f'item indeks:1 (kedua) {nim[1]}')
print(f'item indeks:terakhir {nim[len(nim)-1]}')
# akses item indeks negatif
print(f'item indeks:terakhir (-1) {nim[-1]}')
print(f'item indeks:pertama  (-9) {nim[-len(nim)]}' )
print(f'item indeks:1 (-8) {nim[-8]}')
print(f'item indeks:5 (-4) {nim[-4]}')
# akses indeks batas
print(f'item indeks:1,2,... {nim[1:]}')
print(f'item indeks:3,4,... {nim[3:]}')
print(f'item indeks:0,1,2 {nim[:3]}')
print(f'item indeks:0,1,2,3,4 {nim[:5]}')
print(f'item indeks:semua {nim[:]}')
# pengirisan indeks
print(f'item indeks:1,2,3 {nim[1:4]}')
print(f'item indeks:2,3,4 {nim[2:5]}')
print(f'item indeks:[1:8] {nim[1:-1]}')



data = [('M FURQAN RAMADHANU',2023,'Aktif'),
        (90,89,93,97,98,95,96,91),
        ("2023"),
        ('S1-Reguler Sistem Informasi C','Ganjil')]

matkul = ['Agama Islam',
          'Pancasila',
          'Bahasa Indonesia',
          'Wawasan Cinta IPTEK dan IMTAQ',
          'Pengantar Pemrograman',
          'Pengantar Teknologi Informasi',
          'Kalkulus Dasar I',
          'Sains Terpadu',]
sks = [2,2,2,2,3,3,3,3]



# Tambahkan matkul dan sks ke dalam data (pakai append)

print()
print(data[0][0])
print(data[-1][0])
print(data[2][0:])

print()
# Daftar Mata kuliah
print("Daftar Mata kuliah:")
# Mata kuliah 1: Matkul1 dengan jumlah 2 sks
print(f"Mata kuliah 1: {matkul[0]} dengan jumlah {sks[0]} sks")
# Mata kuliah 2: Matkul2 dengan jumlah 3 sks
print(f"Mata kuliah 2: {matkul[1]} dengan jumlah {sks[1]} sks")
# Mata kuliah 3: Matkul3 dengan jumlah 2 sks
print(f"Mata kuliah 3: {matkul[2]} dengan jumlah {sks[2]} sks")
# Mata kuliah 4: Matkul4 dengan jumlah 3 sks
print(f"Mata kuliah 4: {matkul[3]} dengan jumlah {sks[3]} sks")
# Mata kuliah 5: Matkul5 dengan jumlah 3 sks
print(f"Mata kuliah 5: {matkul[4]} dengan jumlah {sks[4]} sks")
# Mata kuliah 6: Matkul6 dengan jumlah .. sks
print(f"Mata kuliah 6: {matkul[5]} dengan jumlah {sks[5]} sks")
# Mata kuliah 7: Matkul7 dengan jumlah .. sks
print(f"Mata kuliah 7: {matkul[6]} dengan jumlah {sks[6]} sks")
# Mata kuliah 8: Matkul8 dengan jumlah .. sks
print(f"Mata kuliah 8: {matkul[7]} dengan jumlah {sks[7]} sks")

print(f"Total SKS: {sum(sks)}")
# Tambah Nilai jadi 8 (pakai append)
data.append(['Nilai', 90,89,93,97,98,95,96,91])

print()
print(f"Nama mahasiswa: {data[0][0]}")
nama_lengkap = "M FURQAN RAMADHANU"
kata_kata = nama_lengkap.split()
inisial = ''.join([kata[0] for kata in kata_kata])
print(f"Inisial {nama_lengkap}: {inisial}")
print(f"NIM {data[0][0]}: {''.join(nim)}")
print(f"Program pendidikan {data[0][0]}: {data[3][0]}")
print(f"Angkatan {data[0][0]} : {data[3][1]}-{data[0][1]}")
print(f"Total sks {data[0][0]}: {sum(sks)}")
print(f"Jumlah nilai {data[0][0]} adalah: {len(data[1])}")
print(f"Data terbesar {data[0][0]} adalah: {max(data[1])}")
print(f"Data terkecil {data[0][0]} adalah: {min(data[1])}")
rata = sum(data[1]) / len(data[1])
print(f"Rata-rata nilai {data[0][0]}: {rata}")