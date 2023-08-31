''' 
dependencies yang perlu diinstall :
1. pip install bs4
2. pip install requests
'''
import requests as r
import csv
from bs4 import BeautifulSoup as soup

url = 'https://id.wikipedia.org/wiki/Daftar_kabupaten_di_Indonesia'
response = r.get(url)
data_source = response.text
output = soup(data_source, 'html.parser')

# Mendapatkan data dari header tabel
table_header = output.table.find_all('th')
headers = [header.text.strip() for header in table_header]

# Mendapatkan data dari isi tabel (isi data berada pada tag 'td' yang diapit tag 'tr')
table_data = []
table_rows = output.find_all('tr')
for row in table_rows:
    data = row.find_all('td')
    fix_data = [tableData.text.strip() for tableData in data]

    # Melewati tag 'tr' pertama yang berisi tag 'th' yang menyebabkan list kosong
    if len(fix_data) == 0:
        continue
    
    # Menambahkan hasil ekstrak data tabel ke dalam list tabel data
    table_data.append(fix_data)

# Membuat sebuah file csv bernama kabupaten.csv
with open('kabupaten.csv', 'w', newline='') as file:
    writer = csv.writer(file)

    # Memuat data header tabel dan data isi tabel ke dalam file csv
    writer.writerow(headers)
    writer.writerows(table_data)