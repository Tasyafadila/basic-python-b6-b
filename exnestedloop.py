list_nilai = [80,90,70]
for x in list_nilai:
    print(x)
print ("==========")
list_nilai_2 = [
    [80,90,70],
    [90,70,100],
    [100,67,98]
]

for x in list_nilai_2:
    print(x*2)
print("=======")

print("=======")
for i in range(len(list_nilai_2)):
    for j in range (len(list_nilai_2[i])):
        print(list_nilai_2 [j][i]*2)

