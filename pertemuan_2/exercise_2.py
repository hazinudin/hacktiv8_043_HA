status = 'y'
foods = list()

while status == 'y':
    order = input("Mau makan apa: ")
    foods.append(order)
    status = input("Pesan lagi? (y/n)")
    status = status.lower()

print ("Pesanan anda {0} buah".format(len(foods)))
for food in foods:
    print("anda memesan: {0}".format(str(food)))