usia = input("Masukan umur anda:")


if int(usia) >= 1 and int(usia) <= 3:
    print("kamu adalah bayi")

elif int(usia) >= 4 and int(usia) <= 5:
    print("kamu adalah balita")

elif int(usia) >= 6 and int(usia) <= 10:
    print("kamu adalah anak-anak")

elif int(usia) >= 11 and int(usia) <= 16:
    print("kamu adalah remaja")

elif int(usia) >= 17 and int(usia) <= 45:
    print("kamu sudah dewasa")

elif int(usia) >= 46 and int(usia) < 70:
    print("selamat kamu sudah TUA")

else:
    print("KAMU SUDAH MOKAD")
