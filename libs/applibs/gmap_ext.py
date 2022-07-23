from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from libs.applibs import utils,gmap_clear
from time import sleep
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
    maxValue = 1
    maxErr = 2
    for i in range(1,maxValue+1):
        print("Page :: ",i)
        try:
            scrollbox = WebDriverWait(driver, 10).until(
                                    EC.presence_of_element_located((By.XPATH, "/html/body/div[3]/div[9]/div[9]/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[1]"))
                                    )
            last_ht ,ht = 0,1
            while last_ht != ht:
                last_ht = ht
                sleep(5)
                ht = driver.execute_script("""
                arguments[0].scrollTo(0,arguments[0].scrollHeight);
                return arguments[0].scrollHeight;
                """,scrollbox)
                utils.PROGRESS_VALUE = round((last_ht/ht)*100)

            scrape(driver.page_source)
            # gmap_clear.clean_data()
            
            
            # nextBtn = WebDriverWait(driver, 10).until(
            #                         EC.presence_of_element_located((By.XPATH, "/html/body/div[3]/div[9]/div[9]/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[2]/div/div[1]/div/button[2]/img"))
            #                         )
            # nextBtn.click()
        except:
            if maxErr == 0:
                utils.PROGRESS_VALUE = 100
                break
            
            maxErr -= 1
            continue
    
    driver.close()
    gmap_clear.clean_data()
    gmap_clear.sort_data()


