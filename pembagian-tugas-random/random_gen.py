from bs4 import BeautifulSoup

# with open('this.html','rb') as f: 
#     content = f.read()
# soup = BeautifulSoup(content,'html.parser')
# names = soup.find_all('td')
# for name in names: 
#     print(name.text)
blm = '«BLM MENGISI KUESIONER»'

with open('kumpulan.txt','rb') as f: 
    contents = f.readlines()
nama = []
for content in contents:
    content = str(content,'utf-8')
    # print(type(content))
    # print(content)
    if 'MENGISI' in content: 
        # print(content)
        nama.append(content[:-24].upper())

print(nama)
awal = 43
akhir = 78
nomor = []
for i in range(34): 
    awal+=1
    nomor.append('4.'+str(awal))

print('jumlah angka: ',len(nomor))
print('jumlah nama:', len(nama))



from random import shuffle,randint
import pprint
random_number = randint(1,100)
for i in range(random_number):
    shuffle(nama)
    # shuffle(nomor)
    dict={}
    for angka, names in zip(nomor,nama):
        dict[angka] = [names]

pprint.pprint(dict)
print('number of iteration: ',random_number)



