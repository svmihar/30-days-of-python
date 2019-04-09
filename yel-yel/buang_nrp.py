with open('nama.txt') as f:
    list_nama = f.readlines()
    list_nama = [x.strip() for x in list_nama]
print(len(list_nama))
nama, nrp = [],[]
koleksi=[]
for kata in list_nama: 
    kumpulan={}
    if kata.isdigit(): 
        nrp.append(kata)
    else:
        nama.append(kata)

print(f'panjang nama: {len(nama)} \npanjang nrp: {len(nrp)}')


for na, nr in zip(nama, nrp): 
    kumpulan = {}
    kumpulan['nama'] = na
    kumpulan['nrp'] = nr
    koleksi.append(kumpulan)
dict_nrp={'15':'3',
'16':'2',
'17':'1',
'18':'NON-WARGA',
'14':'3',
'13':'3',
'12':'3',
'11':'3',
'10':'3'
}


for index, nama in enumerate(koleksi): 
    print(nama['nama'])

# for i in range(len(koleksi)): 
#     if len(koleksi[i]['nrp'])>10: 
#         print(dict_nrp[(koleksi[i]['nrp'][4:6])])
#     else: 
#         print(dict_nrp[(koleksi[i]['nrp'][2:4])])


#STI 52: //*[@id="mG61Hd"]/div/div[2]/div[2]/div[2]/div/div[2]/div/content/div/div[1]/label/div/div[1]/div[3]/div
#STI-51: //*[@id="mG61Hd"]/div/div[2]/div[2]/div[2]/div/div[2]/div/content/div/div[2]/label/div/div[1]/div[3]/div
#STI-50: //*[@id="mG61Hd"]/div/div[2]/div[2]/div[2]/div/div[2]/div/content/div/div[3]/label/div/div[1]/div[3]/div