url = 'https://docs.google.com/forms/d/e/1FAIpQLSc39V6O8bcyNPOG98egLOJgDxcIyP57Pkjoy6AQv6ivElASZw/viewform'

from selenium import webdriver
import time, random
import pandas as pd
import datetime

# driver = webdriver.PhantomJS(r'C:/Users/PEMODELAN-01/Downloads/phantomjs.exe')
driver = webdriver.Chrome(r'C:/Users/PEMODELAN-01/Downloads/chromedriver.exe')
with open('nama.txt','r') as f: 
    x = f.readlines()
nama = x
print(len(nama))
random.shuffle(nama)
pancasila = 'Bahwa sesungguhnya kemerdekaan itu ialah hak segala bangsa dan oleh sebab itu, maka penjajahan diatas dunia harus dihapuskan karena tidak sesuai dengan perikemanusiaan dan perikeadilan. Dan perjuangan pergerakan kemerdekaan Indonesia telah sampailah kepada saat yang berbahagia dengan selamat sentosa mengantarkan rakyat Indonesia ke depan pintu gerbang kemerdekaan negara Indonesia, yang merdeka, bersatu, berdaulat, adil dan makmur. Atas berkat rahmat Allah Yang Maha Kuasa dan dengan didorongkan oleh keinginan luhur, supaya berkehidupan kebangsaan yang bebas, maka rakyat Indonesia menyatakan dengan ini kemerdekaannya. Kemudian daripada itu untuk membentuk suatu pemerintah negara Indonesia yang melindungi segenap bangsa Indonesia dan seluruh tumpah darah Indonesia dan untuk memajukan kesejahteraan umum, mencerdaskan kehidupan bangsa, dan ikut melaksanakan ketertiban dunia yang berdasarkan kemerdekaan, perdamaian abadi dan keadilan sosial, maka disusunlah kemerdekaan kebangsaan Indonesia itu dalam suatu Undang-Undang Dasar negara Indonesia, yang terbentuk dalam suatu susunan negara Republik Indonesia yang berkedaulatan rakyat dengan berdasar kepadak etuhanan Yang Maha Esa, kemanusiaan yang adil dan beradab, persatuan Indonesia, dan kerakyatan yang dipimpin oleh hikmat kebijaksanaan dalam permusyawaratan/perwakilan, serta dengan mewujudkan suatu keadilan sosial bagi seluruh rakyat Indonesia.'
random.shuffle(nama)
pancasila = pancasila.split(' ')
print(pancasila)


def lesgo(namanya): 
    driver.get(url)
    kata_random = pancasila[random.randint(0,len(pancasila))]
    elem = driver.find_element_by_xpath("//*")
    source_code = elem.get_attribute("outerHTML")
    # print(source_code)
    if 'computer network which appear to be in violation' in source_code: 
        # print(source_code)
        print('you are banned, sleeping for 10 minutes from '+ str(time.time()))
        time.sleep(600)
    else: 
        print('lanjut')
        driver.find_element_by_xpath('//*[@id="mG61Hd"]/div/div[2]/div[2]/div[1]/div/div[2]/div/div[1]/div/div[1]/input').send_keys(namanya)
        driver.find_element_by_xpath('//*[@id="mG61Hd"]/div/div[2]/div[2]/div[2]/div/div[2]/div/content/div/div[1]/label/div/div[1]/div[3]/div').click()
        driver.find_element_by_xpath('//*[@id="mG61Hd"]/div/div[2]/div[2]/div[3]/div/div[2]/div[1]/div[2]/textarea').send_keys('z5801')
        driver.find_element_by_xpath('//*[@id="mG61Hd"]/div/div[2]/div[3]/div[1]/div/div/div[2]').click()
        time.sleep(2)
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