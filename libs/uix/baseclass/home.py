
from kivymd.uix.list import  OneLineListItem
from kivymd.uix.screen import MDScreen

from libs.applibs import utils
from libs.applibs import gmap_ext,gmap_clear

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
        with open(f"{utils.FILENAME}_CleanGmap.csv") as FileData:
            for item in FileData.readlines():
                    self.ids.search_items.add_widget(
                    OneLineListItem(text=item)
                )

    def progressBar(self):
        while True:
            self.ids.progress_bar.value = utils.PROGRESS_VALUE
            

        
        
    def search_fields(self,region_field,keyword_field,code_filed,url_field):
        
        utils.BackThread = threading.Thread(target=self.back_processing)
        utils.ListThread = threading.Thread(target=self.progressBar)
        
        utils.FILENAME = region_field
        utils.REAGION = region_field
        utils.KEYWORDS = keyword_field
        utils.CODE = code_filed
        utils.URL = url_field
        self.show_alert_dialog()
        utils.BackThread.start()
        utils.ListThread.start()
            

        