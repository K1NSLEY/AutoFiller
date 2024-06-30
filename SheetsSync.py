#libs
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

planilha = 'a.xlsx'

os.system('cls')
user01 = input("Digite o Nome de usuário: ")
time.sleep(1)
os.system('cls')

passw01 = input('Digite a Senha: ')
time.sleep(1)
os.system('cls')


chromedriver_path = input('Digite o caminho do chromedriver, digite 0 para padrão: ')
if chromedriver_path == '0':
    chromedriver_path = "C:/chromedriver.exe"

# Verifica se o caminho do ChromeDriver é válido
if not os.path.exists(chromedriver_path):
    print("O caminho do ChromeDriver não é válido. Por favor, verifique o caminho e tente novamente.")
else:
    time.sleep(1)
    os.system('cls')  # Limpa a tela no Windows
    print(f"ChromeDriver configurado no caminho: {chromedriver_path}")
    

webdriver = webdriver.Chrome()
webdriver.get('https://fill.dev/form/login-simple')




act1 = webdriver.find_element(By.NAME, 'username')
act1.send_keys(user01)
time.sleep(1)
act2 = webdriver.find_element(By.NAME, 'password')
act2.send_keys(passw01)
time.sleep(1)
act3 = webdriver.find_element(By.XPATH, '//*[@id="app"]/main/div/div/div/div/div[2]/form/div[3]/div/button')
act3.click()
time.sleep(1)
act4 = webdriver.find_element(By.XPATH, '//*[@id="navbarSupportedContent"]/ul/li[2]/a')
act4.click()
time.sleep(1)
act5 = webdriver.find_element(By.XPATH, '//*[@id="navbarSupportedContent"]/ul/li[2]/ul/li[1]/a')
act5.click()
time.sleep(1)
act6 = webdriver.find_element(By.ID, 'email')
act6.send_keys(user01 + "@teste.com.br")      
time.sleep(1)
act6 = webdriver.find_element(By.ID, 'password')
act6.send_keys(passw01 + "Senha 2")     
time.sleep(1)                         
input('Press enter to close')