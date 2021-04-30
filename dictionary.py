#dictionary created
pelanggan_dict={
    "nama":"tasya",
    "umur":20,
    #key   #value
}
#list created ex
pelanggan_list=[]

#akses dictionary
print(pelanggan_dict["nama"])
print(pelanggan_dict["umur"])

#pelanggan_list.append(pelanggan_dict)
#print(pelanggan_list)

#in
for i in range(2):
    nama=input("masukkan nama anda :")
    umur=input("masukkan umur anda :")
    data={
    "nama":nama,
    "umur":umur,
    }
    pelanggan_list.append(data)
print (pelanggan_list[0])

for i in pelanggan_list:
    print("nama pelanggan:",i[nama])
    print("umur pelanggan:",i[umur])