# Web Form Filling Automation with Python

This project uses Python to automate the filling of web forms. It uses libraries such as `pandas` for data manipulation and `selenium` for web browser interaction. The script reads data from an Excel file (`.xlsx`) and fills out an online form with this data.

## Required Libraries

Make sure to have the following libraries installed:
    
```sh
pip install pandas selenium
pip install webdriver
pip install getpass
pip install glob
pip install sys
pip install os
```

## Top of Code

First, we import all the necessary libraries for the script:

```python    
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
import getpass
import time
import glob
import sys
import os
```

## Recize window CMD
The resize_window function resizes the console window:

```python
def resize_window(lines, columns):
    os.system(f'mode con: cols={columns} lines={lines}')
resize_window(15, 120)
```
The `resize_window` function adjusts the size of the console window on a Windows system.

- **Function Purpose:**
  - The `resize_window` function sets the console window size based on the provided `lines` (height) and `columns` (width) parameters.

- **Usage:**
  - Example usage to set the console window to 15 lines tall and 120 columns wide:
    ```python
    resize_window(15, 120)
    ```

- **Explanation:**
  - The function uses `os.system` to execute a command (`mode con:`) in the Windows command prompt.
  - `cols={columns}` and `lines={lines}` specify the number of columns and lines for the console window, respectively.

### Function to List Possible `.xlsx` Files

This Python function, `list_possibles`, retrieves a list of `.xlsx` files located in the current directory.

```python
def list_possibles():
    current_directory = os.getcwd()
    possibles_xlsx = glob.glob(os.path.join(current_directory, '*.xlsx'))
    return possibles_xlsx
```




### Handling `.xlsx` File Selection

This section of Python code manages the selection of a `.xlsx` file from the current directory.

```python
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
```

### Reading and Processing Data from Excel File

This section of Python code reads data from a selected `.xlsx` file using pandas and prepares for web form filling.

```python
df = pd.read_excel(chosen)
print("A lista a ser preenchida na Web é a segunte: ")
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
time.sleep(0.5)
```

### Automating Web Form Login

This section of Python code automates the login process on a web form using Selenium WebDriver.

```python
chrome = webdriver.Chrome()
chrome.get("https://fill.dev/form/login-simple")
time.sleep(2)
login = chrome.find_element(By.XPATH, '//*[@id="username"]')
password = chrome.find_element(By.XPATH, '//*[@id="password"]')
oklogin = chrome.find_element(By.XPATH, '//*[@id="app"]/main/div/div/div/div/div[2]/form/div[3]/div/button')
login.send_keys(assi_log)
password.send_keys(assi_psw)
oklogin.click()
time.sleep(2)
```
### Navigating to a Specific Page After Login

This section of Python code navigates to a specific page on the web application after successful login using Selenium WebDriver.

```python
inden = chrome.find_element(By.XPATH, '/html/body/div/nav/div/div/ul/li[4]/a')
inden.click()
inden2 = chrome.find_element(By.XPATH, '/html/body/div/nav/div/div/ul/li[4]/ul/li/a')
inden2.click()
time.sleep(1)
os.system('cls')
```

### Automating Form Filling on Web Application

This section of Python code automates the process of filling out a web form using data from a DataFrame (`df`) with Selenium WebDriver.

```python
for index, row in df.iterrows():
    # Locate form input elements using Selenium WebDriver
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
    
    # Print current record being processed
    print("Preenchendo: " + str(index + 1) + "° valor da tabela")
    
    # Fill form fields with data from the current row of the DataFrame
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
    
    # Indicate that current record has been filled
    print(str(index + 1) + "° valor" + " Preenchido!")
    print(" ")
    
    # Click on submit button
    submit2.click()
    time.sleep(1)
    
    # Perform navigation to restart the form-filling process
    restart1 = chrome.find_element(By.XPATH, '//*[@id="navbarSupportedContent"]/ul/li[4]/a')
    restart2 = chrome.find_element(By.XPATH, '//*[@id="navbarSupportedContent"]/ul/li[4]/ul/li/a')
    restart1.click()
    restart2.click()
    time.sleep(1)
```
**Functionality:**
- Iterates through each row `(index, row)` in the DataFrame `(df)`, representing data to be entered into a web form.

- Uses Selenium WebDriver to locate specific form input elements `(act1 to act10)` on the web page using their IDs `(By.ID)` or XPath `(By.XPATH)`.
- Sends data from the current row `(row["NOME"], row["NOMEDOMEIO"], ...)` to their respective form fields using `send_keys()`.
Clicks on the submit button `(submit2.click())` to submit the filled form.
Navigates to restart the form-filling process for the next record using navigation elements (restart1, restart2).

**Usage:**
- This code segment automates the process of filling out a web form repeatedly with data from an Excel file, clicking submit, and resetting the form for the next entry.
- It's useful for tasks requiring repetitive data entry or testing of web forms.
Note:
- Ensure that the IDs `('given-name', 'additional-name', 'family-name', etc.) and XPaths used ('/html/body/div/main/div/div/div/div/div[2]/form/...')` match the actual structure of the web form. Adjust these identifiers as necessary if the form structure changes.
Adjust the timing `(time.sleep())` as needed to ensure proper synchronization with the web page's responsiveness.
Consider error handling and robustness improvements for real-world applications, such as handling form submission errors or dynamic changes in the web page structure.


## End and quit
```python

chrome.quit()
```