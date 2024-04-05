# NIM      : 19235026
# Nama     : Agitha Nupa Ganendra
# Kelas    : 19.1A.24
# Sistem Informasi

#Latihan 1

#Contoh Opertor Penugasan
nilai_pangkat = int(input("masukkan nilai:"))
pangkat = int(input("masukkan pangkat:"))
nilai_pangkat **= pangkat
print(nilai_pangkat)

#Contoh Operator Logika
x = 5
print("x>3 and x<10")
#mengembalikkan Benar karena 5 lebih besar dari 3 DAN 5 kurang dari 10

#Contoh Operator Bitwise
a = 10
b = 20
print("a &= b")

#Contoh Operator Identitas
x = ["apel" , "pisang"]
y = ["apel" , "jeruk"]
z = x
print("x is z")
#mengembalikkan True karena z adalah objek yang sama dengan x
print("x is not y")
#mengembalikkan False karena x bukan objek yang sama dengan y

#Contoh Operator Keanggotaan
var1 = "python"
print("t ada di var1", "t" in var1)