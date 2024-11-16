# Program Which Starwars Character Are You
# Mencari tahu khodam starwars berdasarkan watak kamu

print("lets find out which starwars character are you")

# ready loop

while True:
    ready= input("are you READY?(type ready or no): ")
    converted_ready= ready.lower()
    if converted_ready == "ready":
        break
    elif converted_ready == "no":
        print("ill wait until ur ready")
    else:
        print("u cannot enter anything other than ready or not")

# mendefinisikan skor
score=0

# soal pertama
print("choose ur favorite color:")
print("a. green")
print("b. blue")
print("c. red")
print("d. black")
ans1= input("answer: ")
converted_ans1= ans1.lower()

# algoritma validator jawaban
while converted_ans1 not in ['a', 'b', 'c', 'd']:
    print("you can only input a,b,c,d!")
    print("choose ur favorite color:")
    print("a. green")
    print("b. blue")
    print("c. red")
    print("d. black")
    ans1= input("answer: ")
    converted_ans1= ans1.lower()
if converted_ans1 == "a":
    score += 1
    pass
elif converted_ans1 == "b":
    score += 2
    pass
elif converted_ans1 == "c":
    score -= 1
    pass
elif converted_ans1 == "d":
    score -= 2
    pass

# soal kedua
print("which planet in starwars do you prefer:")
print("a. dagobah")
print("b. tattoine")
print("c. coruscant")
print("d. mandalore")
ans2= input("answer: ")
converted_ans2= ans2.lower()

# algoritma validator jawaban
while converted_ans2 not in ['a', 'b', 'c', 'd']:
    print("you can only input a,b,c,d!")
    print("which planet in starwars do you prefer:")
    print("a. dagobah")
    print("b. tattoine")
    print("c. coruscant")
    print("d. mandalore")
    ans2= input("answer: ")
    converted_ans2= ans2.lower()
if converted_ans2 == "a":
    score += 1
    pass
elif converted_ans2 == "b":
    score += 2
    pass
elif converted_ans2 == "c":
    score -= 1
    pass
elif converted_ans2 == "d":
    score -= 2
    pass

# soal ketiga
print("which starwars droids do you fw the most:")
print("a. R2-D2")
print("b. R4-P17")
print("c. C-3PO")
print("d. hatin droids")
ans3= input("answer: ")
converted_ans3= ans3.lower()

# algoritma validator jawaban
while converted_ans3 not in ['a', 'b', 'c', 'd']:
    print("you can only input a,b,c,d!")
    print("which starwars droids do you fw the most:")
    print("a. R2-D2")
    print("b. R4-P17")
    print("c. C-3PO")
    print("d. hatin droids")
    ans3= input("answer: ")
    converted_ans3= ans3.lower()
if converted_ans3 == "a":
    score += 1
    pass
elif converted_ans3 == "b":
    score += 2
    pass
elif converted_ans3 == "c":
    score -= 1
    pass
elif converted_ans3 == "d":
    score -= 2
    pass

# penentuan karakter berdasarkan jumlah skor
if score>3:
    print("you are OBI-WAN KENOBI")
elif 0<score<=3:
    print("you are YODA")
elif score==0:
    print("you are JAR-JAR BINKS")
elif -3<=score<0:
    print("you are ANAKIN SKYWALKER")
else:
    print("you are DARTH MAUL")