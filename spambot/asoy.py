import time 
import random
from selenium import webdriver
import time, datetime
driver = webdriver.PhantomJS(r'C:/Users/PEMODELAN-01/Downloads/phantomjs.exe')
# driver = webdriver.Chrome(r'C:/Users/PEMODELAN-01/Downloads/chromedriver.exe')
url='https://docs.google.com/forms/d/e/1FAIpQLSfX1Su6kN32ic6OxhpQcwpCVOS2omgeAH9RXnL9mgYtQRYI6g/viewform'

import pandas as pd 
with open('nama.txt','r') as f: 
    x = f.readlines()
nama = x
print(len(nama))
random.shuffle(nama)
minat = ['SAYA MINAT','\"SAYA MINAT\"','saya minat']
def lesgo(name): 
    driver.get(url)
    driver.find_element_by_xpath('//*[@id="mG61Hd"]/div/div[2]/div[2]/div[2]/div/div[2]/div/div[1]/div/div[1]/input').send_keys(name)
    driver.find_element_by_xpath('//*[@id="mG61Hd"]/div/div[2]/div[2]/div[3]/div/div[2]/div/content/div/div[{}]/label/div/div[1]/div[3]/div'.format(random.randint(1,4))).click()
    driver.find_element_by_xpath('//*[@id="mG61Hd"]/div/div[2]/div[2]/div[4]/div/div[2]/div/content/div/div[1]/label/div/div[1]/div[3]/div').click()
    driver.find_element_by_xpath('//*[@id="mG61Hd"]/div/div[2]/div[2]/div[5]/div/div[2]/div/content/div/div[{}]/label/div/div[1]/div[3]/div'.format(random.randint(1,3))).click()
    driver.find_element_by_xpath('//*[@id="mG61Hd"]/div/div[2]/div[2]/div[6]/div/div[2]/div/div[1]/div/div[1]/input').send_keys(minat[random.randint(0,2)])
    # time.sleep(1)
    driver.find_element_by_xpath('//*[@id="mG61Hd"]/div/div[2]/div[3]/div[1]/div/div/content').click()
    driver.delete_all_cookies()

start = time.time()
for i, name in enumerate(nama): 
    try:        
        print(str(i)+'/'+str(len(nama)),datetime.datetime.now(),'\n'+name)
        lesgo(name)
        print()
    except:
        pass
end = time.time()
print('done', end-start)
driver.quit()