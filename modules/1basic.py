# ------ chapter 1: variable -------

# strings
ur_name= "Jacko"

# integers
age= 17

# float
sisa_duit= 15.0

# boolean
boy= False

print(f"My name is {ur_name}, Im {age} years old, i have ${sisa_duit} currently in my m-banking")

if boy:
    print("im a boy")
else:
    print("im not a boy")



# ------ chapter 2: typecasting ------

age= str(age)
ur_name= bool(ur_name)
sisa_duit= str(sisa_duit)
sisa_duit+= age

print(type(age))
print(type(ur_name))
print(sisa_duit)

# u can add up float and int variable
# converting into boolean variable will always results: True except u didnt type anything



# ----- chapter 3: math library -----

# calculating volume of triangle pyramid and ball volume
# triangle pyramid

import math

length= float(input("type in the length of your triangle pyramid: "))
width= float(input("type in the width of your triangle pyramid: "))
height= float(input("type in the height of your triangle pyramid: "))

cuboid_volume= length*width*height
pyramid_volume= cuboid_volume/3

print(f"the volume of your triangle pyramid is: {pyramid_volume}")

# ball volume

radius= float(input("type in the radius of the ball: "))

ball_volume= 4/3*math.pi*radius**3

print(f"the ball volume is: {ball_volume}")

# calculating hypotenuse of pythagorean triangle

X= float(input("enter the first side of triangle: "))
Y= float(input("enter the second side of triangle: "))

hypotenuse= math.sqrt(pow(X,2)+pow(Y,2))
print(f"your triangle hypotenuse is: {hypotenuse}cm")