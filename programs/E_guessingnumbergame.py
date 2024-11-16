# Program menebak angka random dari sistem

# mengimpor library random
import random

# meminta sistem secara random memilih angka 1-100
a= random.choice(range(1,101))


# loop menebak sampai ketemu
while True:
    user_input= input("ENTER YOUR GUESS (exit to quit): ")

    try:
        user_input= int(user_input)
        if user_input - a > 5:
            print("guess lower!")
        if user_input - a <-5:
            print("guess higher!")
        if 0 < user_input - a <= 5:
            print("almost there, guess lower!")
        if -5 <= user_input - a < 0:
            print("almost there, guess higher!")
        if user_input== a:
            print("CONGRATS")
            break

# apabila input berupa string
    except ValueError:
        if user_input.lower() == "exit":
            print("oke silahkan")
            break
        else:
            print("enter a valid number")
