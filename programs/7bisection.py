# Program bisection
# terinspirasi dari matkul MA1101 oleh Dr. Math Fajar Yuliawan
# untuk mencari perkiraan terdekat akar dari suatu fungsi

# mendefinisikan fungsi bisection
def bisection(f, a, b, e=10**-100, N=100):

# kondisional apabila bilangan tidak terletak di antara a dan b
    if f(a) * f(b)>=0:
        print("use another guess range")

# loop mencari nilai tengah
    for n in range (1,N):
        mid = (a + b) /2

# menentukan nilai tengah dengan jarak yang lebih mendekati akar
        if abs(f(mid)) < e:
            return mid
        else:
            if f(mid) * f(a) < 0:
                b = mid
            elif f(mid) * f(b) < 0:
                a = mid
    return mid

# input perkiraan 1, 2, dan fungsi matematis
a= float(input("input first guess: "))
b= float(input("input second guess: "))
functioninput= input("input function e.g x**2-17: ")

# mengolah input fungsi menjadi fungsi f(x)
f= lambda x : eval(functioninput)

# print akar
root = bisection(f, a, b)
print(f"the root approximation is {root}")