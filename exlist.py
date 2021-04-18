mylist=[7,8,9]
print(mylist)

mylist.append(10)
mylist.append(11)
mylist.append(12)
print(mylist)

tambah_angka_baru = int(input("masukkan:"))
mylist.append(tambah_angka_baru)
mylist[0]=tambah_angka_baru
print(mylist)