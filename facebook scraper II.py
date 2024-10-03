# #####PARTE II.5: entremos a nuestra cuenta y entremos al perfil de un amigo (no se olviden rellenar los txt y descargar los comprimidos)
# #inspirado en https://github.com/harismuneer/Ultimate-Facebook-Scraper
# #pip install selenium
from sys import exit
import calendar
import time
import os
os.chdir(r"C:\Users\Biblioteca\Desktop\Practica\WebScrapping\facebook scraper II")
import platform
import sys
import time

from selenium import webdriver
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys


def login(email, password):
    """ Logging into our own profile """

    try:
        global driver

        options = Options()

        #  Code to disable notifications pop up of Chrome Browser
        options.add_argument("--disable-notifications")
        options.add_argument("--disable-infobars")
        options.add_argument("--mute-audio")
        options.add_argument("--start-maximized")
        # options.add_argument("headless")

        try:
            driver = webdriver.Chrome(options=options)
            print("you logged in. Let's rock")
        except:
            print("you need web driver!")
            exit()

        driver.get("https://en-gb.facebook.com")
        # filling the form
        driver.find_element(By.ID, "email").send_keys(email)
        driver.find_element(By.ID, "pass").send_keys(password)
        # clicking on login button
        driver.find_element(By.NAME, 'login').click()
    except:
        print("maybe something is wrong")

# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------

def main():
    with open('credentials.txt') as f:
        email = f.readline().split('"')[1]
        password = f.readline().split('"')[1]

        if email == "" or password == "":
            print("Your email or password is missing. Kindly write them in credentials.txt")
            exit()

    busqueda = [line.split("/")[-1] for line in open("input.txt", newline='\n')]
    
    if len(busqueda) > 0:
        print("\nStarting Scraping...")

        login(email, password)
        time.sleep(5)
        buscador = driver.find_element(By.XPATH, "//input[@placeholder='Buscar en Facebook']")
        buscador.send_keys("city lab biobio")
        time.sleep(5)
        buscador.send_keys(Keys.ENTER)
        print (buscador)
    else:
        print("Input file is empty.")
    


# -------------------------------------------------------------
# -------------------------------------------------------------
# -------------------------------------------------------------

if __name__ == '__main__':
    main()
    input("Presiona Enter para cerrar el navegador...")