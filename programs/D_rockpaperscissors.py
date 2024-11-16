# Program untuk bermain gunting batu kertas melawan python

# mengimpor library random
# random adalah library bawaan python, jadi tidak diperlukan external installation

import random

# mendefinisikan gambar gunting batu dan kertas sebagai elemen string

rock = """ 
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___) 
 """

paper = """ 
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)

"""

scissors = """ 
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

"""

# memasukkan gambar ke dalam array

gambar= [rock, paper, scissors]

# meminta user input

print("SLAMAT DATANG DI PRMAINAN GUNTNG BATU KRETAS!!!")
user_choice= input("type rock, scissors, atau paper: ")

# print gambar pilihan kita

if user_choice== "rock":
    print(f"km memilih: {rock}")

elif user_choice== "scissors":
    print(f"km memilih: {scissors}")

elif user_choice== "paper":
    print(f"km memilih: {paper}")

# randomize pilihan sistem

com_choice= random.choice(gambar)

# print gambar pilihan sistem

if com_choice== rock:
    print(f"bot memilih: {rock}")

elif com_choice== scissors:
    print(f"bot memilih: {scissors}")

elif com_choice== paper:
    print(f"bot memilih: {paper}")

# kondisional menang kalah seri

if user_choice== "rock" and com_choice== scissors:
    print("selamat km menang lawan bot!")
elif user_choice== "scissors" and com_choice== paper:
    print("selamat km menang lawan bot!")
elif user_choice== "paper" and com_choice== rock:
    print("selamat km menang lawan bot!")
elif user_choice== "paper" and com_choice== scissors:
    print("alamak km kalah lawan bot!")
elif user_choice== "scissors" and com_choice== rock:
    print("alamak km kalah lawan bot!")
elif user_choice== "rock" and com_choice== paper:
    print("alamak km kalah lawan bot!")
else:
    print("draw!")
