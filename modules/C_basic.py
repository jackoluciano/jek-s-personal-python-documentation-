# ------ chapter 6: while loop -----

enter_name= input("whos ur favorite boi? ")

while not enter_name== "jeko":
    print("you picked the WRONG BOI")
else:
    print("have a nice day!")
# and it will loop forever, except

enter_name2= input("whos ur favorite boi? ")

while not enter_name2== "jeko":
    print("you picked the WRONG BOI")
    enter_name2= input("whos ur favorite boi? ")
else:
    print("have a nice day!")




# ------- chapter 7: for ---------

# dictionary, terdiri atas kunci:nilai (bersifat mutable, namun elemennya immutable)
murid= {'zulfa':'cacing' , 'jacko':'manusia' , 'fauzan':'manusia' , 'awan':'bebek'} 

# Strategi: mengiterasi copy
for users,jenis in murid.copy().items():
    if jenis=='cacing' or jenis=='bebek':
        del murid[users]

print(murid)

# list dan delete list (bersifat mutable)
my_list = [1, 2, 3, 4, 5]
del my_list[1:3]  # my_list is now [1, 4, 5] karena starting dari urutan 1 (2) tetapi urutan 3 (4) tetap ada dalam list.

print(my_list)




# --------- chapter 8: init function ----------

# __init__ adalah fungsi bawaan untuk mengatur nilai awal objek secara otomatis tanpa perlu dipanggil kembali
# nilai diatur dalam tuple yang bersifat immutable

# contoh : referensi buku
class book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def book_notif(self):
        return f"i got a book called {self.title} for you, written by {self.author}, released on {self.year}!"

my_book= book("laskar pelangi", "andrea hirata", 2006)

print(my_book.book_notif())

# contoh lain: notif di edunex

class edunex:
    def __init__(self, matkul, judul, deadline, dosen):
        self.matkul = matkul
        self.judul = judul
        self.deadline = deadline
        self.dosen = dosen

    def edunexnotif(self):
        return f"you got a new task {self.judul} from {self.matkul} by {self.dosen} ended in {self.deadline}"

edunex_task= edunex("MA1101", "TUGAS KALKULUS 01", "10 AGUSTUS", "PAK FAJAR")
print(edunex_task.edunexnotif())
