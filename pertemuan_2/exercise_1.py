a = input("Masukkan angkan: ")
#a = int(a)

print (type(a))
print("Nilai a: {0}".format(a))
remainder = a%2

if remainder > 0:
	print("Nilai a adalah bilangan ganjil")
else:
	print("Nilai a adalah bilangan genap")