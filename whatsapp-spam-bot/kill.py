from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://web.whatsapp.com/')

name = input('Enter the name of user or group : ')
msg = input('Enter your message : ')
count = int(input('Enter the count : '))

input('Enter anything after scanning QR code')

user = driver.find_element_by_xpath('//*[@id="pane-side"]/div/div/div/div[1]/div/div/div[2]/div[1]/div[1]/span'.format(name))
user.click()

msg_box = driver.find_element_by_class_name('_3F6QL')

for i in range(count):
    msg_box.send_keys(msg)
    button = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button')
    button.click()
    print(str(i) + " message sent " + "\nsent:" + msg)