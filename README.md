# Web Form Filling Automation with Python

This project uses Python to automate the filling of web forms. It uses libraries such as `pandas` for data manipulation and `selenium` for web browser interaction. The script reads data from an Excel file (`.xlsx`) and fills out an online form with this data.

## Required Libraries

Make sure to have the following libraries installed:
    
    python
    pip install pandas selenium
    pip install webdriver
    pip install getpass
    pip install glob
    pip install sys
    pip install os

## Top of Code

First, we import all the necessary libraries for the script:

    import pandas as pd
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    import getpass
    import time
    import glob
    import sys
    import os
## hello