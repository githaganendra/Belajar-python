#Studi kasus : Penjualan Tiket

#Input
pembeli = input("masukan nama pembeli : ")
no_hp = input("masukan nomer hp : ")
jurusan = input("masukan kode jurusan [SBY/BL/LMP] : ").upper()
jumlah_beli = int(input("masukan jumlah tiket yang dibeli : "))
uang_masuk = int(input("uang masuk :"))
nama_kota = " "
harga_jurusan = 0

#Proses
if jurusan == "SBY" :
    nama_kota = "Surabaya"
    harga_jurusan = 300000
elif jurusan == "BL" :
    nama_kota = "Bali"
    harga_jurusan = 350000
elif jurusan == "LMP" :
    nama_kota == "Lampung"
    harga_jurusan = 500000
else:
    print("jurusan tidak ada")
    exit()

diskon = 0
if jumlah_beli >=3:
    diskon = 0.1 *(jumlah_beli * harga_jurusan)

total = (jumlah_beli * harga_jurusan) - diskon
if total > uang_masuk:
    print("uang tidak cukup")
    exit()

uang_kembali = uang_masuk - total

#Cetak hasil
print("------------------------------------------")
print("          PENJUALAN TIKET BUS")
print("                   XYZ")
print("------------------------------------------")
print("Nama Pembeli  : ",pembeli)
print("No. Handphone : ",no_hp)
print("Kode Jurusan yang dipilih : ",jurusan)
print("Nama Kota Tujuan : ",nama_kota)
print("Harga         : ",harga_jurusan)
print("Jumlah Beli   : ",jumlah_beli)
print("------------------------------------------")
print("potongan yang didapat : ",diskon)
print("Total Bayar   : ",total)
print("Uang Masuk    : ", uang_masuk)
print("Uang Kembali  : ", uang_kembali)
print("-----------------------------------------")

