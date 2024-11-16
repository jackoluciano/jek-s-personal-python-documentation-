# Program mengecek judul dan harga buku
# scrap data dari website latihan

# impor library 
import requests # request untuk berinteraksi dengan API
from bs4 import BeautifulSoup # BeautifulSoup untuk parsing data, dalam hal ini properti html

# mendefinisikan url dan meminta respon ke API url yg bersangkutan
url = 'https://books.toscrape.com/'
response = requests.get(url)

# pengecekan status code http
if response.status_code == 200: # 200 OK

# menggunakan tools html parser dari BeautifulSoup dari response text
    soup = BeautifulSoup(response.text, 'html.parser')
    
# mengambil data produk pada class tertentu di web, dalam hal ini <class="product_pod">
    first = soup.find_all(class_="product_pod")

# mendefinisikan list kosong yang akan diolah
    pairsbrack= []

# mengambil judul dan harga lewat html propertiesnya
    for firs in first:
        title = firs.find("h3").find("a")["title"]
        price = firs.find(class_="price_color").text.strip()

# memasukkan ke list kosong    
        pairs = pairsbrack.append((title, price))

else:
    print(f"Gagal mengambil data, status code: {response.status_code}")

# sortir dan formatting data

pairsbrack.sort(key=lambda pair:pair[1])
for i in range(len(pairsbrack)):
    judul, harga = pairsbrack[i]
    print(f"{judul:<100} : {harga:>8} ")