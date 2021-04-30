def menghitung_lingkaran(r):
    phi=22/7
    L=phi*r*r
    K=phi*(r*2)
    return L,K
r=int(input("masukkan jari-jari:"))
lingkaran=menghitung_lingkaran(r)

text=("luas dengan r{}cm adl {:.2f} \u00b2 dan kll {:.2f}cm".format(lingkaran[0],lingkaran[1])
print(text)