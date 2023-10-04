print("================== isi data sendiri ==============")
nama = input("nama :")
nim = input("NIM :")
jurusan = input("Jurusan : ")
alamat = input("Alamat = ")
a = input("masukan nilai:")

print("====== Hasil data diatas adalah ======")
print("Nama =  " + str(nama))
print("Nim =  " + str(nim))
print("jurusan =  " + str(jurusan))
print("Alamat =   " + str(alamat))
if int(a) > 60:
    print("anda lulus:" + str(a))

else:
    print("anda tidak lulus:" + str(a))
