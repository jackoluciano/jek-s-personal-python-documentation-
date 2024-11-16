# Program mengecek funfact tentang sebuah angka
# mengambil rekapan dari rapidapi.com dengan key dan host yang telah disediakan

# menggunakan request library
import requests

# mengimpor url dan headers yang dibutuhkan berupa key dan host
baseurl= "https://numbersapi.p.rapidapi.com/"
header= {
    'x-rapidapi-host' : 'numbersapi.p.rapidapi.com',
	'x-rapidapi-key' : 'cc6ab9ac7fmshad9a4dc9a1cdd26p1355f0jsncb183ad94797'
}

# mendefinisikan fungsi get info untuk variabel tertentu
def getinfo(num):

# mengaitkan link dengan variabel
    url = f"{baseurl}{num}/math"
    response = requests.get(url, headers=header)
    print(response.text)

# seharusnya dicek dulu status codenya, namun asumsikan saja http 200 OK
# apabila program tidak berjalan, berarti ada masalah request

# input dan assign variabel lalu jalankan fungsi
number = input("enter a number: ")
getinfo(number)