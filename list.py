mylist=[7,8,9]
print(mylist)

mylist.append(10)
mylist.append(11)
mylist.append(12)
print(mylist)

print(mylist[1])

print(len(mylist))

#mylist=[10.11.12]
#       0  1   2

tambah_angka_baru = int(input("masukkan:"))
mylist.append(tambah_angka_baru)
mylist[0]=tambah_angka_baru
print(mylist)