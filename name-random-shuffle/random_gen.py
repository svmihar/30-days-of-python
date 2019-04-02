from pprint import pprint
import random

with open('kumpulan.txt','rb') as f: 
    contents = f.readlines()

blm = '«BLM MENGISI KUESIONER»'
nama = []
for content in contents:
    content = str(content,'utf-8')
    if 'MENGISI' in content: 
        nama.append(content[:-24].upper())

#remove karena gak pernah masuk
nama.remove('MUHAMAD FARRAS HANINDITO RUKMANTORO')

soal = [1,1,2,2,3,3,4,4,5,5]
dict_soal = {
    '1': 'TEORI PERSEDIAAN',
    '2': 'TEORI ANTRIAN',
    '3': 'TEORI PERMAINAN',
    '4': 'GOAL PROGRAMMING',
    '5': 'DYNAMIC PROGRAMMING'
    }
random.shuffle(nama)
random.shuffle(soal)


kelompok = []
for i in range(0,len(nama),3):
    kelompok.append(nama[i:i+3])
anggota_sisa = kelompok[-1]
print(f'tersisa: {anggota_sisa}')
kelompok.remove([anggota for anggota in anggota_sisa])

daleman = dict()
fix = dict()
for i in range(len(kelompok)): 
    fix[i+1]= {
        'anggota kelompok': kelompok[i],
        'soal': dict_soal.get(str(soal[i])),
        }

for anggota in anggota_sisa: 
    angka = random.randint(0,len(fix))
    print(f'memasukkan {anggota} ke {angka}')
    fix[angka]['anggota kelompok'].append(anggota)


pprint(fix)