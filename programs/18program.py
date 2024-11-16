# Program mengecek kategori berat badan berdasarkan bodyweight lb and kg
N = int(input("masukkan N: "))

for i in range(N):
    bebas = input(f"Masukkan berat petinju ke-{i+1}")
    if "kg" in bebas:
        bebas_baru= int(bebas.split(" kg")[0])*2.205
    if "lb" in bebas:
        bebas_baru= int(bebas.split(" lb")[0])
    if bebas_baru>=200:
        print(f"Petinju ke-{i+1} masuk ke dalam Heavyweight")
    elif 154<=bebas_baru<200:
        print(f"Petinju ke-{i+1} masuk ke dalam Middleweight")
    elif 0<bebas_baru<154:
        print(f"Petinju ke-{i+1} masuk ke dalam Lightweight")




# Program menentukan N faktorial
N = int(input("masukkan nilai N: "))
Mbaru=1

for i in range(1,N+1):
    if i >=2:
        M= Mbaru*(i)
        Mbaru= M

print(Mbaru)




# Program menentukan apakah sebuah bilangan adalah bilangan prima pada range tertentu
N = int(input("Masukkan N: "))
ranges= int(input("Masukkan range: "))
m = 0

for i in range(2, ranges):
    if N%i == 0:
        m+=1

if m ==1:
    print("bilangan prima")
else:
    print("bukan bilagan prima")




# Program menentukan deret fibonacci sebanyak N-buah
n= int(input("masukkan N: "))
M = [1,1]

for i in range(n-2):
    M += [M[i] + M[i+1]]

if n ==1:
    print([M[0]])
elif n ==2:
    print([M[0],M[1]])
else:
    print(M)

# Program menentukan deret fibonacci dengan fungsi
def fib(n):
    result=[]
    a,b= 0,1

    while a < n:
        result.append(a)
        a,b = b,a+b
    return result
    
print(fib(int(input("masukkan N: "))))




# mengecek bilangan terdapat dalam suatu array
M= int(input("Masukkan jumlah array: "))
list= []
ditemukan= False

for i in range(M):
    N = int(input("Masukkan elemen array: "))
    list += [N]

cari = int(input("bilangan apa yang mau kamu cari: "))

for i in range(M):
    if cari == list[i]:
        print(f"bilangan ditemukan, pada indeks ke-{i}")
        ditemukan = True

if ditemukan == False:
    print("bilangan tidak ditemukan")




# Program membuat persegi dengan sisi sepanjang a
a= int(input("masukkan angka: "))

# baris
for i in range(a):

# kolom
    for j in range (a):
        print("*", end="")

# membuat baris baru    
    print()




# Program mencari nilai 10^i terdekat dengan N
N = int(input("Masukkan nilai N: "))

# segera break ketika 10^i sudah melebihi N
for i in range(100):
    if 10**i>N:
        print(10**i)
        break
    else:
        continue




# Program membuat segitiga dengan alas M
M= int(input("Masukkan N: "))

# baris
for i in range(1,M+1):

# kolom
    for j in range(1,i+1):
        print(j, end="")

# membuat baris baru
    print()




# Program Reverse Array
G = int(input("Masukkan N: "))
f = [0 for i in range(G)]

# Mengganti nilai array dengan input
for i in range(G):
    f[i] = int(input("masukkan nilai: "))

# fungsi reverse
f.reverse()
print(f)