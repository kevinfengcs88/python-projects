from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random

PATH = "C:\Program Files (x86)\chromedriver.exe"

letters = []
for one in range(97, 123):
    char = chr(one)
    letters.append(char)

bot_count = int(input("How many bots would you like: "))
PIN = input("Enter game PIN: ")

i = 0
drivers = []
while i < bot_count:
    drivers.append(webdriver.Chrome(PATH))
    i += 1

for driver in drivers:
    current_driver = driver
    current_driver.get("https://kahoot.it/")
    gamePIN = current_driver.find_element_by_id("game-input")
    gamePIN.send_keys(PIN)
    gamePIN.send_keys(Keys.RETURN)
    try:
        element = WebDriverWait(current_driver, 5).until(EC.presence_of_element_located((By.ID, "nickname")))
        gameNAME = current_driver.find_element_by_id("nickname")
        NAME = ""
        k = 0
        while k < 3:
            NAME += str(random.randint(0, 9))
            NAME += random.choice(letters)
            k += 1
        gameNAME.send_keys(NAME)
        gameNAME.send_keys(Keys.RETURN)
    finally:
        pass
