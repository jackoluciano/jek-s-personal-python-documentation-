# Program mencari kombinasi banyak cara berbagi permen

# mengimpor library math
import math

# text msg
print("hi! i can count how many ways you can share your candies to different amount of ppl")

# input banyak permen
candies= int(input("how many candies do you have: "))

# kondisional jumlah permen
if candies <=0:
    print("im so sorry take this 🍬")

if candies >0:

# input jumlah orang
    people= int(input("how many people are there: "))
    result= math.factorial(people) / (math.factorial(candies) * math.factorial(people - candies)) 

# kondisional kondisi jumlah orang terhadap jumlah permen
    if people < candies:
        print("better eat it yourself")
    elif people == candies:
        print("you have exactly 1 way to share ur candies!")
    else:
        print(f"you have {result:.0f} ways to share ur candies!")