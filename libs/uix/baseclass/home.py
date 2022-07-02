from kivymd.uix.list import ImageLeftWidget, OneLineListItem
from kivymd.uix.screen import MDScreen

from libs.applibs import utils

utils.load_kv("home.kv")

class Home_Screen(MDScreen):
    
    def search_account(self,search_field):
        """
        this method use when search button pressed search_field
        contain data in string that you want to search on hamster server
        """

        # for dummy search item [------
        
        if search_field != "":
            onelineW= OneLineListItem(text=f"{search_field}")
            self.ids.search_items.add_widget(onelineW)

        
        
        # #  ----- ] end dummy search
    
    