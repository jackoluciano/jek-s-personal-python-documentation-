# --------- chapter 12: Algoritma Timeout menggunakan library Threading -------------------
# fungsi Thread dapat menjalankan 2 aktivitas secara bersamaan dalam suaru sistem, contoh meminta user input dan menjalankan timer
import threading    

while True:
    
# mendefinisikan fungsi dan global variable
    def getinput():
        global userinput
        userinput= input("input something: ")

# userinput bernilai None selagi tidak diberi input
# userinput dijalankan bersamaan dengan timeout selama 10 detik
    userinput= None
    thread= threading.Thread(target=getinput)
    thread.start()
    thread.join(timeout=10)

# kondisional setelah timeout
    if userinput==None:
        break
    else:
        print(f"your input is: {userinput}")
        break

print("you're out of loop.")




# Algoritma break function dengan fungsi dan return
def breakfunc():
    while True:
        userinput= input("enter something (yes to quit): ")
        if userinput=="yes":
            return

# memanggil fungsi
breakfunc()
print("Yay")