from kivymd.uix.list import  OneLineListItem
from kivymd.uix.screen import MDScreen

from libs.applibs import utils
from libs.applibs import gmap_ext,gmap_clear

from kivymd.uix.dialog import MDDialog
from kivy.clock import Clock

from time import sleep
import threading
import os

utils.load_kv("home.kv")


class Home_Screen(MDScreen):

    def __init__(self, **kw):
        super().__init__(**kw)
        self.OLDList = list()
        self.srcListItem = list()
        self.ListData = list()

    def show_alert_dialog(self):
        # Show Alert When Search button click and Brower is opening
        self.dialog = MDDialog(
                title = "Browser starting.",
                text="Wait plz... ",
                
                )
        self.dialog.open()
        
    
    def updateOnClock(self,dt):
        # Update Appliction UI on Clock frame
        self.ids.progress_bar.value = utils.PROGRESS_VALUE
        if utils.PROGRESS_VALUE == 100 and utils.isFileSaved:

            self.dialog = MDDialog(
                        title = "Done...",
                        text="Files Saved",
                        
                        )
            self.dialog.open()
            
            utils.PROGRESS_VALUE = 0
            utils.isFileSaved = False
        
    
    def ListItemTouch(self,touch,item):
        # for List item click event
        self.ids.filename_field.text = touch.text

    def sortAllFiles(self):
        for CSVFile in os.listdir():
            if ".csv" in CSVFile:
                FileData = open(CSVFile)
                sortfile = set(FileData.readlines())
                WriteFile = open(CSVFile,"w")
                WriteFile.writelines(sorted(list(sortfile)))
                FileData.close()
                WriteFile.close()
                
                
    def back_processing(self):
        # This Process in Other Thread for backgrond proceess of web scraping
        driver = gmap_ext.driver_init()
        for urldata in self.ListData:
            utils.FILENAME = urldata["filename"]
            utils.REAGION = urldata["region"]
            utils.CODE = urldata["code"]
            # utils.Filter = urldata["filter"]
            utils.URL = urldata["url"]
            
            gmap_ext.start_scraping(driver,utils.URL)

            
        
        self.sortAllFiles()
        utils.isFileSaved = True
        driver.close()
        
    def clearForm(self):
        #self.ids.code_field.text = ""
        #self.ids.filter_field.text = ""
        self.ids.url_field.text = ""
        
    def addSearchList(self,region_field,code_filed,url_field,filter_field):
        for item in str(filter_field).split(","):
            utils.Filter.append(item)
        
        URLData = {
            "filename" : region_field,
            "region" : region_field,
            "code" : code_filed,
            "url" : url_field,
            "filter" : str(filter_field).split(",")

        }     
        self.ids.search_items.add_widget(
            OneLineListItem(text=f"{URLData['filename']} | {URLData['code']} |{URLData['filter']} | {URLData['url']}")
        )
        self.ListData.append(URLData)
        self.clearForm()


        pass
    def search_fields(self):
        # WebScarping Search filed text box
        utils.BackThread = threading.Thread(target=self.back_processing)
        
        self.show_alert_dialog()
        utils.BackThread.start()
        
        


        




