#libs
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
import getpass
import time
import glob
import sys
import os

def recize_window(linhas, colunas):
    os.system(f'mode con: cols={colunas} lines={linhas}')

recize_window(15, 120)

def list_possibles():
    current_directory = os.getcwd()
    possibles_xlsx = glob.glob(os.path.join(current_directory, '*.xlsx'))
    return possibles_xlsx
possibles_xlsx = list_possibles()

if not possibles_xlsx:
    os.system('cls')
    print("Nenhum arquivo .xlsx encontrado, encerrando o executável")
    time.sleep(1)
    print("Favor posicionar um arquivo .xlsx NO MESMO DIRETÓRIO que o executável!")
    time.sleep(5)
    sys.exit()
else:
    os.system('cls')
    print("Arquivos .xlsx encontrados no diretório atual:")
    for idx, arquivo in enumerate(possibles_xlsx, start=1):
        print(f"{idx}. {os.path.basename(arquivo)}")

    choice = int(input("Escolha o número do arquivo que deseja usar: ")) - 1
    chosen = possibles_xlsx[choice]

    print(f"Você escolheu: {os.path.basename(chosen)}")

df = pd.read_excel(chosen)
print("A lista a ser preenchida na Web é a segunte: ")
time.sleep(2)
for index, row in df.iterrows():
    print(
        str(row["TECNICO"]) + " " +
        str(row["DESCRIPT"]) + " " +
        str(row["DEFEITO"]) + " " +
        str(row["SERVICE"]) + " " +
        str(row["CODIGO"]) + " " +
        str(row["OS11"]) + " "
    )
    time.sleep(0.1)
time.sleep (0.5)
for i in range(3):
    os.system('cls')
    print("Agora, faça login através desse terminal CMD")
    time.sleep(0.5)
    os.system('cls')
    time.sleep(0.5)
    i + 1

assi_log = input("Insira seu nome de usuário no ASSIST: ")
os.system('cls')
time.sleep(1)
assi_psw = getpass.getpass("Insira sua senha de acesso ASSIST: ")
os.system('cls')
print("Navegador Web aberto em 3 segundos!")


chrome = webdriver.Chrome()
chrome.get("https://pontonet.assistonline.com.br/index.php?url=/bin/at/pesquisaOs.php")
time.sleep(2)
login = chrome.find_element(By. ID, 'usuario_login')
password = chrome.find_element(By. XPATH, '//*[@id="login_form"]/table/tbody/tr[2]/td/input')
oklogin = chrome.find_element(By. XPATH, '//*[@id="login_form"]/table/tbody/tr[5]/td/input')
login.send_keys(assi_log)
password.send_keys(assi_psw)
oklogin.click()
time.sleep(2)

inden = chrome.find_element(By. XPATH, '//*[@id="pesq_os"]')
inden.click()
time.sleep(1)
os.system('cls')

for index, row in df.iterrows():
    act1 = chrome.find_element(By.XPATH, '//*[@id="os"]')
    act1.send_keys(row["OS11"])
    submit2 = chrome.find_element(By.XPATH, '//*[@id="formPesquisaOS"]/table/tbody/tr[14]/td/img')
    submit2.click()
    act2 = chrome.find_element(By.XPATH, '//*[@id="rodaScript"]/table/tbody/tr[3]/td[4]/a/img')
    act2.click()
    print(" ")

    act3 = chrome.find_element(By.XPATH, '//*[@id="nomeTecnico"]')
    act3.send_keys(row["TECNICO"])

    act4 = chrome.find_element(By.XPATH,'//*[@id="descrDefeito"]')
    act4.send_keys(row["DESCRIPT"])

    act5 = chrome.find_element(By.XPATH, '//*[@id="td_defeito"]/select')
    act5.send_keys(row["DEFEITO"])

    act6 = chrome.find_element(By.XPATH,'//*[@id="td_solucao"]/select')
    act6.send_keys(row["SERVICE"])

    act7 = chrome.find_element(By.XPATH, '//*[@id="AVAL"]/table/tbody/tr/td/table[3]/tbody/tr[1]/td/table[1]/tbody/tr[4]/td[1]/input')
    act7.send_keys(row["CODIGO"])

    act8 = chrome.find_element(By.XPATH,'//*[@id="AVAL"]/table/tbody/tr/td/table[3]/tbody/tr[1]/td/table[1]/tbody/tr[2]/td[3]/input[1]')
    act8.click()

    act9 = chrome.find_element(By.XPATH,'//*[@id="button_1"]')
    act9.click()

    act10 = chrome.find_element(By.XPATH,'//*[@id="cont_nfEntrada"]/table[1]/tbody/tr/td[2]').getText()
    input(act10)
    act11 = chrome.find_element(By.XPATH,'//*[@id="cont_nfEntrada"]/table[2]/tbody/tr[2]/td/table[1]/tbody/tr[2]/td/input')
    act11.send_keys(act10)

    act12 = chrome.find_element(By.XPATH,'//*[@id="cont_nfEntrada"]/table[2]/tbody/tr[2]/td/table[3]/tbody/tr/td/input')
    act12.click()
    



        

    time.sleep(1)
    restart1 = chrome.find_element(By. XPATH, '//*[@id="pesq_os"]')
    restart1.click()
    time.sleep(1)
chrome.quit()