from bs4 import BeautifulSoup
from selenium import webdriver

from libs.applibs import utils,gmap_clear
import asyncio
def driver_init():
    # Selenium Driver init
    driver = webdriver.Firefox() 
    return driver

def write_data(data1):
    with open(f"{utils.FILENAME}_Gmap.csv","a") as csv_file:
        csv_file.write(f"{data1}\n")

def scrape(site):
    siteHtml = BeautifulSoup(site,"html.parser")
    # , attrs={'class':'btn_whatsapp'}
    for atag in siteHtml.find_all("span"):
        try:
            href = atag
            print(href)
            write_data(href)
        except:
            continue

def start_scraping(driver,url):
    driver.get(url)
    # https://www.google.com/maps/search/toronto++car+dealers/@43.7179846,-79.5181437,11z/data=!3m1!4b1
    for i in range(1,5):
        print("Page :: ",i)
        scrape(driver.page_source)
        gmap_clear.clean_data()
    
    driver.close()

