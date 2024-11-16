# Program membuat tabel fungsi kuadrat dengan fungsi

# menginisiasi fungsi kuadrat
def kuadrat(x):
    x2= (x**2) - (2*x) + 5
    return x2

# meminta input
a = int(input("Masukkan A: "))
b = int(input("Masukkan B: "))

if a<b:
    print("A harus lebih kecil dari B")

# mengulang tabel fungsi
for i in range(a,b+1):
    print(f"f({i}) = {kuadrat(i)}")

# Program membuat segitiga pascal
# sebuah angka merupakan hasil penjumlahan angka di kiri dan di atasnya
# angka di kolom dan baris pertama adalah 1

# menginisiasi fungsi kuadrat
def pascal(n):

# baris pertama bernilai 1
    x = [1,1,1,1]

    for i in range(1,4*(n-1)+1):
    
# kolom pertama bernilai 1
        if i%4 ==1:
            x += [1]

# pertambahan angka di kiri dan di atasnya
        else:
            x += [x[i-1] + x[i+2]]
    
# formatting
    for y in range(n):
        print(f"{x[4*y]} {x[4*y +1]} {x[4*y +2]} {x[4*y +3]}")
    
# memanggil fungsi pascal berdasarkan input jumlah N
pascal(int(input("masukkan N: ")))