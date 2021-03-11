from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import requests
import time                 #for primitive waits

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://www.amazon.com/")
print(driver.title)

search = driver.find_element_by_id("twotabsearchtextbox")
search.send_keys("bag")
search.send_keys(Keys.RETURN)

try:
    element = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "nav-top")))
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36'}
    result = requests.get(driver.current_url, headers=headers)
    soup = BeautifulSoup(result.content, "html.parser")
    print(result.status_code)

    for d in driver.find_elements_by_xpath("/html/body/div[1]/div[2]/div[1]/div[2]/div/span[4]/div[2]/div[4]"):
        name = d.find('span', attrs={'class': 'a-size-base-plus a-color-base a-text-normal'})
        price = d.find('span', attrs={'class': 'a-offscreen'})
        rating = d.find('span', attrs={'class': 'a-icon-alt'})
        print(name)
        print(price)
        print(rating)
    print("this happened")
finally:
    driver.quit()
