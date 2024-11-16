# Program Lagu Anak Ayam dalam berbagai macam tipe iterasi
# jangan lupa block code klau mau coba

# using FOR

N = 5

for i in range(N,0,-1):
    print("Anak ayam turunlah", i)
    if i>1:
        print("Mati satu tinggallah", i-1)
    else:
        print("Mati satu tinggal induknya")

# using WHILE

while N>1:
    N-=1
    print("Anak ayam turunlah", N+1)
    print("Mati satu tinggallah", N)
else:
    print("Anak ayam turunlah", N)
    print("Mati satu tinggal induknya")

# using DO-WHILE

while True:
    N-=1
    print("Anak ayam turunlah", N+1)
    print("Mati satu tinggallah", N)
    if N==1:
        print("Anak ayam turunlah", N)
        print("Mati satu tinggal induknya")
        break