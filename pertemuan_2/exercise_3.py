from random import randint

lower_range = 1
upper_range = 10
answer = randint(lower_range, upper_range)
attempt = 0
correct_answer = False

print("Saya memikirkan suatu angka.")
print("Ayo tebak angka Saya.")

while not correct_answer:
    guess = input("Masukkan tebakan anda ({0}-{1}) : ".format(lower_range, upper_range))
    guess = int(guess)
    attempt = attempt + 1

    if guess < answer:
        print("Tebakan terlalu kecil")
    elif guess > answer:
        print("Tebakan terlalu besar")
    elif guess == answer:
        correct_answer = True

print("Tebakan anda benar!")
print("Anda menebak {0} kali.".format(str(attempt)))