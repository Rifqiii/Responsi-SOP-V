# 5200411186 - Rifqi Helmi Fadhil

prgm = {}

print("============= Program Round Robin =============")
jmlh = int(input("Jumlah Program : "))

def create(programKey, programValue):
    prgm[programKey] = programValue
    print("Program Berhasil Dimasukkan!")

x = 1
while x <= jmlh :
  programKey = str(input("\nNama Program : "))
  programValue = int(input("Brush Time : "))
  create(programKey, programValue)
  x += 1

quantum = int(input("\nQuantum Time : "))

def sort():
    return sorted(prgm.items(), key=lambda item: item[1], reverse=False)

def move(programKey, programValue):
    prgm[programKey] = programValue

print("\n================= Hasil Running =================")
prog = sort()
for key, value in prog:
    print("Nama Program : {}\t\tBrush Time: {}".format(key,value))