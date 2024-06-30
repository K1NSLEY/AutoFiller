#libs
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

#set paths
chromedriver_path = 'C:/chromedriver.exe'
webdriver = webdriver.Chrome()
webdriver.get('')

user01 = ('')
passw01 = ('')

act1 = webdriver.find_element(By.NAME, 'usuario_login')
act1.send_keys(user01)
act2 = webdriver.find_element(By.NAME, 'usuario_senha')
act2.send_keys(passw01)
act3 = webdriver.find_element(By.NAME, 'Submit')
act3.click()
input('Press enter to close')