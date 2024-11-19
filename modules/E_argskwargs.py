# ---------chapter 10: positional and keywords only arguments ----------------

# di belakang tanda "/" adalah positional only arguments, dipanggil dengan value saja
# di depan tanda "*" adalah keywords arguments, harus dipanggil nama parameternya juga
# di antara tanda "/" dan "*" dapat dipanggil posisinya saja, dapat dipanggil nama parameternya juga

def number(a,b,/,c,*,dfactor):
    print("abc =", a*b*c)
    print("d =", dfactor)
    print("check if abc is factor of d")
    if a*b*c%dfactor==0:
        print("abc is factor of d.")
    else:
        print("abc is NOT factor of d.")

A= int(input("input value of a:"))
B= int(input("input value of b:"))
C= int(input("input value of c:"))
D= int(input("input value of d:"))

# perhatikan bahwa hasilnya akan sama saja
number(A,B,C,dfactor=D)
number(A,B,c=C,dfactor=D)

# ada pula seperator untuk menyisipkan karakter di antara karakter secara otomatis

def kalimat(*argumen, separator=" eh "):
    print(separator.join(argumen))

kalimat("i love you", "you love me", "we are happy family", "with a great big hug", "and a kiss from me to you", "won't you say you love me too", "")





# -------- chapter 11: *args dan **kwargs ---------

# variabel di depan "*" dapat diatur sesuai preferensi, dan dia akan menempati posisi yang sama pd tuple fungsi
# "*" mengartikan arguments, yaitu semua hal yang bersifat positional only selain dari variabel yang diatur 
# "**" mengartikan keyword arguments, yaitu semua elemen di arguments yang memiliki nama parameter dan value

def notif(comment, *message, **harga):
    print(comment, "jeko!")
    for m in message:
        print(m)
    for order in harga:
        print(order, ":", harga[order]) # perhatikan bahwa harga sebagai value yang dijadikan nama untuk variabel **kwargs, bukan order

notif("halo banh", "orderan kamu adalah", sosigg="10k", borgir="20k", pitzah ="30k")

# unpacking argument lists
# objective: memanggil *args dengan a=[] dan memanggil **kwargs dengan b={}

def notif2(comment, *message):
    print(comment, "jeko!")
    for m in message:
        print(m)

list= ["halo banh", "orderan kamu adalah", "sosigg : 10k", "borgir : 20k", "pitzah : 30k"]
notif2(*list)

def notif3(comment, comment2, **harga):
    print(comment, "jeko!")
    print(comment2)
    for order in harga:
        print(order, ":", harga[order])

dictionary={"comment":"halo banh", "comment2":"orderan kamu adalah", "sosigg": "10k", "borgir" : "20k", "pitzah" : "30k"}
notif3(**dictionary)
