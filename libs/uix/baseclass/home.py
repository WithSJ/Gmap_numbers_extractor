
from kivymd.uix.list import  OneLineListItem
from kivymd.uix.screen import MDScreen

from libs.applibs import utils
from libs.applibs import gmap_ext

from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog

from time import sleep
import threading

utils.load_kv("home.kv")


class Home_Screen(MDScreen):

    def show_alert_dialog(self):
        # buttons=[MDFlatButton(text="OK")],
        # on_release=(lambda obj: self.dialog.dismiss())
        self.dialog = MDDialog(
                title = "Browser starting.",
                text="Wait plz... ",
                
                )
        self.dialog.open()
        

    def back_processing(self):
        gmap_ext.start_scraping(gmap_ext.driver_init(),utils.URL)

    def updateList(self):
        
        while True:
            listItem = utils.SEARCH_ITEM
            for item in listItem:
                self.ids.search_items.add_widget(
                    OneLineListItem(text=item)
                )
            # newlistItem = utils.SEARCH_ITEM
            # listItem = newlistItem.difference(listItem)
    
    def search_fields(self,region_field,keyword_field,code_filed,url_field):
        
        utils.BackThread = threading.Thread(target=self.back_processing)
        # utils.ListThread = threading.Thread(target=self.updateList)
        
        utils.FILENAME = region_field
        utils.REAGION = region_field
        utils.KEYWORDS = keyword_field
        utils.CODE = code_filed
        utils.URL = url_field
        self.show_alert_dialog()
        utils.BackThread.start()
        utils.ListThread.start()
        
        
        
        
    