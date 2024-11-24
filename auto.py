import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from tkinter import filedialog
import tkinter as tk
import getpass
import time
import glob
import sys
import os

root = tk.Tk()
root.withdraw()

def recize_window(linhas, colunas):
    os.system(f'mode con: cols={colunas} lines={linhas}')

def list_possibles():
    current_directory = os.getcwd()
    possibles_xlsx = glob.glob(os.path.join(current_directory, '*.xlsx'))
    return possibles_xlsx

possibles_xlsx = list_possibles()

if not possibles_xlsx:
    print("Nenhum arquivo .xlsx encontrado, encerrando o executável.")
    time.sleep(1)
    print("Nenhum arquivo encontrado no diretório, favor escolher outro.")
else:
    os.system('cls')
    print("Arquivos .xlsx encontrados no diretório atual:")
    print("Digite o respectivo número dele ou 0 para selecionar em outro diretório.")
    for idx, arquivo in enumerate(possibles_xlsx, start=1):
        print(f"{idx}. {os.path.basename(arquivo)}")

    choice = int(input("Escolha o número do arquivo que deseja usar: ")) - 1
    if choice == -1:
        arqv_sel = filedialog.askopenfilename(filetypes=[("Arquivos Excel", "*.xlsx")])
        chosen = arqv_sel
    else:
        chosen = possibles_xlsx[choice]

    print(f"Você escolheu: {os.path.basename(chosen)}")


def sel_site():
    site = input(" ")    
    if site == "1":
        site = "https://fill.dev/form/login-simple"
        print("Você escolheu o Teste WebCrowler")
    elif site == "2":
        site = "https://pontonet.assistonline.com.br/"
        print("Você escolheu o AssitsPontonet")

# Aqui, 'chosen' agora contém o caminho correto do arquivo
df = pd.read_excel(chosen)
print("A lista a ser preenchida na Web é a seguinte: ")
time.sleep(2)
for index, row in df.iterrows():
    print(
        str(row["NOME"]) + " " +
        str(row["NOMEDOMEIO"]) + " " +
        str(row["ULTIMONOME"]) + " " +
        str(row["NUMERO"]) + " " +
        str(row["RUA"]) + " " +
        str(row["RUA2"]) + " " +
        str(row["CIDADE"]) + " " +
        str(row["ESTADO"]) + " " +
        str(row["ZIP"]) + " " +
        str(row["PAIS"])
    )
    time.sleep(0.1)
for i in range(3):
    os.system('cls')
    print("Agora, faça login através desse terminal CMD")
    time.sleep(0.5)
    os.system('cls')
    time.sleep(0.5)
    i + 1

os.system('cls')
print("Qual o site deseja utilizar? ")
print("Digite o número de um dos sites abaixo ou cole a URL!")
print("1 - Teste WebCrowler")
print("2 - AssistPontonet")
site = input(" ")
if site == "1":
    site = "https://fill.dev/form/login-simple"
    print("Você escolheu o Teste WebCrowler")
elif site == "2":
    site = "https://pontonet.assistonline.com.br/"
    print("Você escolheu o AssitsPontonet")

assi_log = input("Insira seu nome de usuário no ASSIST: ")
os.system('cls')
time.sleep(1)
assi_psw = getpass.getpass("Insira sua senha de acesso ASSIST: ")
os.system('cls')
print("Navegador Web aberto em 3 segundos!")

chrome = webdriver.Chrome()
chrome.get(site)
time.sleep(2)
login = chrome.find_element(By.XPATH, '//*[@id="username"]')
password = chrome.find_element(By.XPATH, '//*[@id="password"]')
oklogin = chrome.find_element(By.XPATH, '//*[@id="app"]/main/div/div/div/div/div[2]/form/div[3]/div/button')
login.send_keys(assi_log)
password.send_keys(assi_psw)
oklogin.click()
time.sleep(2)

inden = chrome.find_element(By.XPATH, '/html/body/div/nav/div/div/ul/li[4]/a')
inden.click()
inden2 = chrome.find_element(By.XPATH, '/html/body/div/nav/div/div/ul/li[4]/ul/li/a')
inden2.click()
time.sleep(1)
os.system('cls')

for index, row in df.iterrows():
    act1 = chrome.find_element(By.ID, 'given-name')
    act2 = chrome.find_element(By.ID, 'additional-name')
    act3 = chrome.find_element(By.ID, 'family-name')
    act4 = chrome.find_element(By.ID, 'tel')
    act5 = chrome.find_element(By.XPATH, '/html/body/div/main/div/div/div/div/div[2]/form/div[5]/div/input')
    act6 = chrome.find_element(By.ID, 'address-line2')
    act7 = chrome.find_element(By.XPATH, '/html/body/div/main/div/div/div/div/div[2]/form/div[7]/div/input')
    act8 = chrome.find_element(By.ID, 'address-level1')
    act9 = chrome.find_element(By.ID, 'postal-code')
    act10 = chrome.find_element(By.ID, 'country')
    submit2 = chrome.find_element(By.XPATH, '//*[@id="app"]/main/div/div/div/div/div[2]/form/div[11]/div/button')
    print("Preenchendo: " + str(index + 1) + "° valor da tabela")
    act1.send_keys(row["NOME"])
    act2.send_keys(row["NOMEDOMEIO"])
    act3.send_keys(row["ULTIMONOME"])
    act4.send_keys(row["NUMERO"])
    act5.send_keys(row["RUA"])
    act6.send_keys(row["RUA2"])
    act7.send_keys(row["CIDADE"])
    act8.send_keys(row["ESTADO"])
    act9.send_keys(row["ZIP"])
    act10.send_keys(row["PAIS"])
    print(str(index + 1) + "° valor" + " Preenchido!")
    submit2.click()
    time.sleep(1)
    restart1 = chrome.find_element(By.XPATH, '//*[@id="navbarSupportedContent"]/ul/li[4]/a')
    restart2 = chrome.find_element(By.XPATH, '//*[@id="navbarSupportedContent"]/ul/li[4]/ul/li/a')
    restart1.click()
    restart2.click()
    time.sleep(1)

chrome.quit()
