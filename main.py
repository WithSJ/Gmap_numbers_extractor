"""
Application Devloped by Sandeep Jadam
Email : withsj.in@gmail.com
Made in India Software



"""

#--[Start platform specific code]

from ctypes import util
from kivy.utils import platform

from kivymd.app import MDApp

if platform != 'android':
    from kivy.config import Config
    Config.set("graphics","width",360)
    Config.set("graphics","height",740)
#--[End platform specific code]

#--[Start Soft_Keyboard code ]
"""code for android keyboard. when in android keyboard show textbox 
automatic go to top of keyboard so user can see when he type msg"""
from kivy.core.window import Window

Window.keyboard_anim_args = {"d":.2,"t":"linear"}
Window.softinput_mode = "below_target"
#--[End Soft_Keyboard code ]

from libs.uix.baseclass.home import Home_Screen
from libs.uix.baseclass.root import Root
from libs.applibs import utils
from kivy.clock import Clock


class GmapExtApp(MDApp):
    """
    GmapEXt App start from here this class is root of app.
    in kivy (.kv) file when use app.method_name app is start from here
    """

    def __init__(self, **kwargs):
        super(GmapExtApp, self).__init__(**kwargs)
        self.icon = "Assets\\icon.ico"
        self.APP_NAME = "Gmap Extractor v1.2.3"
        self.COMPANY_NAME = ""
        
    
    
    def build(self):
        """
        This method call before on_start() method so anything
        that need before start application all other method and code 
        write here.
        """
        self.theme_cls.primary_palette = "Blue"
        self.theme_cls.primary_hue = "500"

        self.theme_cls.accent_palette = "Amber"
        self.theme_cls.accent_hue = "500"

        self.theme_cls.theme_style = "Light"
    
        self.screen_manager = Root()
        homeSRC = Home_Screen()
        Clock.schedule_interval(homeSRC.updateOnClock, 0.1)
        self.screen_manager.add_widget(homeSRC)
        
        return self.screen_manager
    
    def on_start(self):
        """
        Anything we want to run when start application that code is here.
        """
        self.screen_manager.change_screen("home")
    
    def on_stop(self):
        if utils.BackThread != None:
            utils.BackThread.killed  = True
            utils.BackThread.join()

if __name__ == "__main__":
    # Start application from here.
    try:
        import pyi_splash
        pyi_splash.update_text("GMAP UI Loaded...")
        pyi_splash.close()
    except:
        pass
    GmapExtApp().run()
    
