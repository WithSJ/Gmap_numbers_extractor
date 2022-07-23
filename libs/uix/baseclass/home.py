from fileinput import filename
from kivymd.uix.list import  OneLineListItem
from kivymd.uix.screen import MDScreen

from libs.applibs import utils
from libs.applibs import gmap_ext,wapp_check

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
        self.ids.wapp_progress_bar.value = utils.WAPP_PROGRESS_VALUE
        
        # try:
        #     DATAFile = set(open(utils.FILENAME).readlines())
        #     InList = set()
        #     if len(InList) != len(DATAFile):
                
        #         for item_name in DATAFile.difference(InList):
        #             self.ids.files_items.add_widget(
        #                 OneLineListItem(text=item_name))
        #         InList = DATAFile
        # except:
        #     pass



        # -------------CODE------------

        # Here add item in list Whatsapp check pannel 
        # File list use to show which file have numbers

        
        self.NEWList = os.listdir()
        if len(self.NEWList) < len(self.OLDList):
            self.ids.files_items.clear_widgets()
            self.OLDList = list()

        if len(self.NEWList) > len(self.OLDList):
            LISTDATA = set(self.NEWList).difference(set(self.OLDList))
            for item_name in LISTDATA:
                if "Numbers" in item_name:
                    self.ids.files_items.add_widget(
                        OneLineListItem(text=item_name, on_touch_down = self.ListItemTouch)
                        )
            self.OLDList = self.NEWList
        #  --------------END------------
    
    def ListItemTouch(self,touch,item):
        # for List item click event
        self.ids.filename_field.text = touch.text

    def back_processing(self):
        # This Process in Other Thread for backgrond proceess of web scraping
        gmap_ext.start_scraping(gmap_ext.driver_init(),utils.URL)
        
    def search_fields(self,region_field,code_filed,url_field):
        # WebScarping Search filed text box
        utils.BackThread = threading.Thread(target=self.back_processing)
        # utils.ListThread = threading.Thread(target=self.progressBar)
        
        utils.FILENAME = region_field
        utils.REAGION = region_field
        utils.CODE = code_filed
        utils.URL = url_field
        self.show_alert_dialog()
        utils.BackThread.start()
        # utils.ListThread.start()
        # Clock.schedule_interval(self.updateOnClock, 0.1)
        
    def wapp_backworking(self,FileName):
        # Whatsapp background working in Thread to check 
        # number on whatsapp or not
        FileData = open(FileName).readlines()
        print(FileData)
        wapp_check.wapp_search(utils.WAPP_Driver,FileData)

    def wapp_search(self,FileName):
        # Whatsapp check btn event
        print(FileName)
        utils.BackThread = threading.Thread(target=self.wapp_backworking,args=[FileName])
        utils.BackThread.start()
        # Clock.schedule_interval(self.updateOnClock, 0.1)

        
    def login_backworking(self):
        # Login Whatsapp
        utils.WAPP_Driver = wapp_check.driver_init()
        utils.WAPP_Driver.get("https://web.whatsapp.com/")
        

    def wapp_login(self):
        #  Login btn event
        utils.BackThread = threading.Thread(target=self.login_backworking)
        utils.BackThread.start()
        self.show_alert_dialog()

        


        
