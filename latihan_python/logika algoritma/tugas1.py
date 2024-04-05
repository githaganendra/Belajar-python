# NIM      : 19235026
# Nama     : Agitha Nupa Ganendra
# Kelas    : 19.1A.24
# Sistem Informasi

bil1 = 60
bil2 = 20
bil3 = 100
bil4 = 40

max = bil1
bil_terbesar = "bil1"
if bil2 > max:
    max = bil2
    bil_terbesar = "bil2"

if bil3 > max:
    max = bil3
    bil_terbesar = "bil3"

if bil4 > max:
    max = bil4
    bil_terbesar = "bil4"

print("bilangan terbesar adalah {} jumlah: {}". format(bil_terbesar,max))