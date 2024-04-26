# NIM      : 19235026
# Nama     : Agitha Nupa Ganendra
# Kelas    : 19.1A.24
# Sistem Informasi

print("PROGRAM HITUNG GAJI KARYAWAN")
print("Nama Karyawan    : TORIK")
print("Golongan Jabatan : 2")
print("Pendidikan       : S1")
print("Jumlah jam kerja : 10")

nama = input("masukan nama : ")
jabatan = int(input("masukan jabatan : "))
pendidikan = input("masukan pendidikan : ")
jam_kerja = int(input("masukan jam kerja : "))
gaji_pokok = 300000
tunjangan_jab = 0
tunjangan_pend = 0
honor_lembur = 0
if jabatan == 1:
    tunjangan_jab = 0.05 * gaji_pokok
elif jabatan == 2:
    tunjangan_jab = 0.10 * gaji_pokok
elif jabatan == 3:
    tunjangan_jab = 0.15 * gaji_pokok
else:
    print("Golongan jabatan tidak ada")
    exit()

if pendidikan == "SMA":
    tunjangan_pend = 0.025 * gaji_pokok
elif pendidikan == "D1":
    tunjangan_pend = 0.5 * gaji_pokok
elif pendidikan == "D2":
    tunjangan_pend = 0.20 * gaji_pokok
elif pendidikan == "S1":
    tunjangan_pend = 0.30 * gaji_pokok
else:
    print("Pendidikan tidak ada")
    exit()

if jam_kerja > 8:
    honor_lembur = (jam_kerja -8) * 3500
else:
    honor_lembur = 0

total = gaji_pokok + tunjangan_pend + tunjangan_jab + honor_lembur

print("===============================================")
print("Karyawan yang bernama      ", nama)
print("Honor yang diterima")
print("Tunjangan jabatan      Rp. ", tunjangan_jab)
print("Tunjangan pendidikan   Rp. ", tunjangan_pend)
print("Honor lembur           Rp. ", honor_lembur)
print("                        --------------------+")
print("Total Gaji             Rp. ", total)
print("(Gaji pokok + tunjangan + lembur)")
print("===============================================")


