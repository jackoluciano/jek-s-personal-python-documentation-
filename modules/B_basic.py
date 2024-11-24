# ------- chapter 4: string methods ------

# Program memvalidasi username
# validate username
# 6-12 characters
# must include at least 1 digit
# must include at least 1 symbol

# string adalah library bawaan python, jadi tidak diperlukan external installation
import string

keluar = False

while keluar == False:
    username= input("enter ur username: ")

    if 6 <= len(username) <= 12:
        print("ur username contains 6-12 characters")
    else:
        print("ur username DOES NOT contain 6-12 characters")

    checkdigit= any(char.isdigit() for char in username)

    if checkdigit:
        print("ur username contains digit")
    else:
        print("ur username DOES NOT contain digit")

    checksymbol= any(char in string.punctuation for char in username)

    if checksymbol:
        print("ur username contains symbol")
    else:
        print("ur username DOES NOT contain symbol")

    if checkdigit and checksymbol and 6 < len(username) < 12:
        print(f"ur new username is {username}")
        keluar = True



# ------ chapter 5: indexing strings ------

phone_num= "1234-5678-9101"

print(phone_num[::-1]) #reverse
print(phone_num[1:5]) #display character 1-5
print(phone_num[::3]) #kelipatan 3




# ------ chapter 6: format specifier {value:flags} ------

harga_1000_robux= 100000

print(f"harga 1000 robux adalah Rp.{harga_1000_robux:>15,.2f}")
print(f"harga 100 robux adalah Rp.{harga_1000_robux/10:>16,.2f}")
print(f"harga 10 robux adalah Rp.{harga_1000_robux/100:>17,.2f}") 

# > untuk rata kanan, < untuk rata kiri, ^ untuk center, , untuk koma tiap ribuan, .2f untuk 2 desimal di belakang koma 
# (beda sm round() adalah round() membulatkan, sedangkan .f bs menambah angka di blkg koma)




# ------- chapter 7: comparison ------

a = 4
b = 5

hasil = a > b
print("is a > b?", hasil)

hasil2 = a < b
print("is a < b?", hasil2)

hasil3 = a == b
print("is a == b?", hasil3)

hasil4 = a != b
print("is a != b?", hasil4)

hasil5 = a is b
print("is a b?", hasil5)

hasil6 = a is not b
print("is a not b?", hasil6)

c = 7
d = 7

print(hex(id(c)))
print(hex(id(d)))

# kalau c dan d bernilai sama, hex id atau identitasnya akan dideteksi sama sehingga python akan merecall memori, beda halnya dg c dsb
