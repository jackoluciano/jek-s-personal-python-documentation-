# algoritma validator input lanjutan
def ask_ok(prompt, retries=4, reminder='Please try again!'):
    while True:
        reply = input(prompt)
        if reply in {'benar', 'ya', 'yes'}:
            return True
        if reply in {'salah', 'tidak', 'no', 'nope'}:
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)

ask_ok("apakah zulfa cacing? ")

# fungsi greet dengan default message namun costumizable
def greet(name, message="hello"):
    print(f"{message}, {name}")

greet("jacko")
greet("zulfa", "oagi")
