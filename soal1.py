# 5200411186 - Rifqi Helmi Fadhil

print("======= Program PetaBit =======")
ram = float(input("\nKapasitas RAM (GB) : "))
blok = float(input("Jumlah PetaBit : "))
os = float(input("Kapasitas OS (GB) : "))
prgm1 = float(input("Kapasitas Program 1 (MB) : "))
prgm2 = float(input("Kapasitas Program 2 (MB) : "))

# Konvert GB to MB
ramv = ram * 1024
osv = os * 1024

# Kapasitas per blok
kbit = ramv / blok

# Pengelolaan RAM
prgm = prgm1 + prgm2
pake = osv + prgm
tpake = ramv - pake

# Pengelolaan PetaBit
blok1 = pake / kbit
blok0 = blok - blok1


print("\n====== Hasil Perhitungan ======")
print("\nTotal RAM :",ram,"GB")
print("Total OS : ",os,"GB")
print("Kapasitas per Blok :",kbit,"MB")
print("Total RAM Terpakai :",pake,"MB")
print("Total RAM Tidak Terpakai :",tpake,"MB")
print("Blok Bernilai 1 :",blok1)
print("Blok Bernilai 0 :",blok0)