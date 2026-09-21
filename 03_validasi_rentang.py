sudut = float(input("Besar sudut dalam derajat: "))

if sudut <= 0 or sudut >= 180:
    print("Masukan ditolak: sudut harus lebih dari 0 dan kurang dari 180.")
    print("Alasannya: sudut yang dimasukkan berada di luar rentang sudut yang valid.")

elif sudut < 90:
    print("Sudut lancip")
    print(f"Alasannya: {sudut}° lebih dari 0° dan kurang dari 90°.")

elif sudut == 90:
    print("Sudut siku-siku")
    print("Alasannya: besar sudut tepat 90°.")

else:
    print("Sudut tumpul")
    print(f"Alasannya: {sudut}° lebih dari 90° dan kurang dari 180°.")
