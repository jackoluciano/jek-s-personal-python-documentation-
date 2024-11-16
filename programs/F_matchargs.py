# Program menghitung luas berbagai bidang datar dengan match args
# match args adalah atribut kelas yang digunakan untuk mendefinisikan daftar nama atribut yang dapat digunakan dalam pattern matching

import math

# membagi pendefinisian ke dalam beberapa kelas
class circle:
    __match_args__= ("radius",)
    
    def __init__(self, radius):
        self.radius= radius

class rectangle:
    __match_args__ = ("width", "height")
    
    def __init__(self, width, height):
        self.width = width
        self.height = height

class triangle:
    __match_args__ = ("base", "height")
    
    def __init__(self, base, height):
        self.base = base
        self.height = height

# fungsi untuk mencocokan bidang datar lalu menghitung per kasus bidang datar
def calculateArea(shape):
    match shape:
        case circle(radius):
            return f"Area of Circle is {math.pi*radius**2}"
        case rectangle(width, height):
            area = width*height
            if area % 1 !=0:
                return f"Area of Rectangle is {round(width*height)}"
            else:
                return f"Area of Rectangle is {width*height}" # ini contoh penggunaan if else di match statement
        case triangle(base, height):
            return f"Area of Triangle is {base*height/2}"
        case _:
            return "unknown shape"

# memasukkan nilai atribut dan print luas daerah   
print(calculateArea(circle(7)))
print(calculateArea(rectangle(7.7,5)))
print(calculateArea(triangle(7,8)))
print(calculateArea("unknown"))
