from selenium import webdriver
from time import sleep
import time
import random
import string

import os 
BASE_DIR = os.getcwd()
print(BASE_DIR)
url = 'https://docs.google.com/forms/d/e/1FAIpQLSdM2YRHaHR5A7-aeT_A4cQ_YNbgpnzD91yY-cylhShS1uUdTA/viewform'

driver = webdriver.Chrome(executable_path=BASE_DIR+'/chromedriver')

driver.get(url)
def berikutnya(): 
    try:
        driver.find_element_by_xpath('//*[@id="mG61Hd"]/div/div[2]/div[3]/div[1]/div[1]/div[2]/content/span').click()
    except :
        print('tidak ada sebelumnya')
        driver.find_element_by_xpath('//*[@id="mG61Hd"]/div/div[2]/div[3]/div[1]/div[1]/div/content').click()

def random_string(stringLength=10):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))

def letsgo(nama,sti_=0): 
    driver.find_element_by_xpath('//*[@id="mG61Hd"]/div/div[2]/div[2]/div[1]/div/div[2]/div/div[1]/div/div[1]/input').send_keys(nama)
    sti = driver.find_element_by_xpath(f'//*[@id="mG61Hd"]/div/div[2]/div[2]/div[2]/div/div[2]/div/content/div/div[{sti_}]/label/div/div[1]/div[3]/div')
    sti.click()
    berikutnya()
    print('halaman 1/5')

    #penting 
    driver.find_element_by_xpath(f'//*[@id="mG61Hd"]/div/div[2]/div[2]/div[3]/div/div[2]/div/content/div/label[{random.randint(1,4)}]/div[2]/div/div[3]').click()
    #digunakan 
    driver.find_element_by_xpath(f'//*[@id="mG61Hd"]/div/div[2]/div[2]/div[4]/div/div[2]/div/content/div/label[{random.randint(1,4)}]/div[2]/div/div[3]/div').click()
    #kondisi 
    driver.find_element_by_xpath(f'//*[@id="mG61Hd"]/div/div[2]/div[2]/div[5]/div/div[2]/div/content/div/label[{random.randint(1,4)}]/div[2]/div/div[3]/div').click()
    #diganti
    diganti = random.randint(1,2)
    print(f'memilih {diganti} sebagai mars')
    driver.find_element_by_xpath(f'//*[@id="mG61Hd"]/div/div[2]/div[2]/div[6]/div/div[2]/div/content/div/div[{diganti}]/label/div/div[1]/div[3]/div').click()
    berikutnya()
    print('halaman 2/5')

    if diganti == 1:
        driver.find_element_by_xpath(f'//*[@id="mG61Hd"]/div/div[2]/div[2]/div[2]/div/div[2]/div/content/div/div[{random.randint(1,2)}]/label/div/div[1]/div[3]/div').click()
        berikutnya()
        print('halaman 4/5')

    else: 
        driver.find_element_by_xpath('//*[@id="mG61Hd"]/div/div[2]/div[2]/div[2]/div/div[2]/div[1]/div[2]/textarea').send_keys(random_string(stringLength=random.randint(10,50)))
        berikutnya()
        print('halaman 3/5')


    driver.find_element_by_xpath('//*[@id="mG61Hd"]/div/div[2]/div[2]/div[2]/div/div[2]/div[1]/div[2]/textarea').send_keys(random_string(stringLength=random.randint(10,50)))
    print('halaman 5/5 selesai')
    berikutnya()
    driver.get(url)

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

j = 0
while True: 
    j+=1
    random.shuffle(koleksi)
    for i, data in enumerate(koleksi): 
        start = time.time()
        if len(data['nrp']) > 10: 
            # print(f'menggunakan {data['nama']} yang angkatan {data['nrp'][4:6]}')
            print(f"{data['nama']}, angkatan {data['nrp'][4:6]}")
            letsgo(data['nama'], sti_=dict_nrp[data['nrp'][4:6]])
        else: 
            # print(f'menggunakan {data['nama']}, yang angkatan {data['nrp'][2:4]}  ')
            print(f"{data['nama']}, angkatan {data['nrp'][2:4]}")
            letsgo(data['nama'], sti_=dict_nrp[data['nrp'][2:4]])

        end = time.time()
        waktu = end - start
        print(f'\n\n\n\nwaktu yang dibutuhkan dalam iterasi ke {i+1} adalah {waktu}\n\n\n\n')
        print(f'TOTAL ITERASI: {j}')
driver.quit()