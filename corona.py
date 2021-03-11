import gspread
from oauth2client.service_account import ServiceAccountCredentials
from bs4 import BeautifulSoup
import requests
import time

scope = ["https://spreadsheets.google.com/feeds","https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)
client = gspread.authorize(creds)
sheet = client.open("coronaprofit").sheet1

def scrape(int1):
    url = input("Enter site: ")
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36'}
    r = requests.get(url, headers=headers)
    print(r.status_code)
    soup = BeautifulSoup(r.content, "html.parser")
    product_price = soup.find(id="priceblock_ourprice").get_text()
    print(product_price)


scrape(5)
sheet.update_cell(1, 2, "updated")

'''
while True:
    
    time.sleep(600)
'''
