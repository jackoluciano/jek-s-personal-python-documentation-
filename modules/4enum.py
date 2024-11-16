# --------- chapter 9: enum library --------------

# enum: singkatan dari enumeration
# nilai atau nama dapat diakses dengan class.(name).name atau class.(name).value

from enum import Enum

# Program pemesanan pizza

# mendefinisikan kelas dan mengassign value ke sebuah nama
class PizzaSize(Enum):
    small = 8
    medium = 10
    big = 12

# mendefinisikan fungsi cost
def Cost(size):
    return f"the cost of {size.name} pizza is {size.value}"

# memanggil name dan value dari small, lalu memanggil diolah dalam fungsi cost
order = PizzaSize.small
print(Cost(order))