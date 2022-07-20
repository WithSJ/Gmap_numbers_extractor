from ast import Num
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
    with open(f"{utils.FILENAME}_WappChecked.csv","a") as csv_file:
        csv_file.write(f"{data1}\n")


def wapp_search(driver,NumberList):
    i=1
    for item in NumberList:
        try:
            Number = str(item).replace("\n","").replace("+","")
            driver.get(f"https://web.whatsapp.com/send?phone=%2B{Number}&text&type=phone_number&app_absent=0")
            
            NumText = WebDriverWait(driver, 10).until(
                                            EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div/div[4]/div/header/div[2]/div/div/span"))
                                            )
            utils.WAPP_PROGRESS_VALUE = round((i/len(NumberList))*100)
            i+=1
            write_data(str(NumText.text).replace(" ",""))
        except:
            continue
            
    # maxValue = 30
    # maxErr = 2
    # for i in range(1,maxValue+1):
    #     print("Page :: ",i)
    #     try:
    #         scrollbox = WebDriverWait(driver, 10).until(
    #                                 EC.presence_of_element_located((By.XPATH, "/html/body/div[3]/div[9]/div[9]/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[1]"))
    #                                 )
    #         last_ht ,ht = 0,1
    #         while last_ht != ht:
    #             last_ht = ht
    #             sleep(2)
    #             ht = driver.execute_script("""
    #             arguments[0].scrollTo(0,arguments[0].scrollHeight);
    #             return arguments[0].scrollHeight;
    #             """,scrollbox)

    #         # gmap_clear.clean_data()
    #         utils.PROGRESS_VALUE = round((i/maxValue)*100)
            
    #         nextBtn = WebDriverWait(driver, 10).until(
    #                                 EC.presence_of_element_located((By.XPATH, "/html/body/div[3]/div[9]/div[9]/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[2]/div/div[1]/div/button[2]/img"))
    #                                 )
    #         nextBtn.click()
    #     except:
    #         if maxErr == 0:
    #             utils.PROGRESS_VALUE = 100
    #             break
            
    #         maxErr -= 1
    #         continue
    
    # driver.close()
    # gmap_clear.clean_data()
    # gmap_clear.sort_data()
