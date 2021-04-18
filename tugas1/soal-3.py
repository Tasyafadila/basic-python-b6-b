a = int(input("Nilai Ujian Teori   = "))
b = int(input("Nilai Ujian Praktek = "))
if a>=70 and b>=70:
    print("Selamat, anda lulus!")
elif a>=70 and b<70:
    print("Anda harus mengulangi ujian praktek.")
elif a<70 and b>=70:
    print("Anda harus mengulangi ujian teori.")
else:
    print("Anda harus mengulangi ujian teori dan praktek.")