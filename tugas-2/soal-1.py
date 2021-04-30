def daftar():
    print("Dartar kontak :")
    print("Nama : Nafi")
    print("No. Telepon : 0812345678")
    print("Nama : joko")
    print ("No. Telepon : 0987654321")
def tambah():
    pelanggan_list=[]
    for i in range(1):
        nama=input("Nama : ")
        nomor=input("No. Telepon : ")
        data={
        "nama":nama,
        "nomor":nomor,
            }
    print("kontak berhasil ditambahkan")

print("Selamat datang!")
print("---Menu---")
print("1. Daftar kontak")
print("2. Tambah kontak")
print("3. keluar")
pilih=int(input ("pilih menu : "))
if(pilih==1):
    daftar()
elif(pilih==2):
    tambah()
elif(pilih==3):
    print("program selesai, sampai jumpa")
else:
    print("menu tidak tersedia")