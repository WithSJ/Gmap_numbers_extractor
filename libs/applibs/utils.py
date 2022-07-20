import os

from kivy.lang import Builder

# Global Variables 
FILENAME = str()
REAGION = str()
KEYWORDS = str()
CODE = str()
URL = str()
SEARCH_ITEM = set()
BackThread=None
ListThread = None
PROGRESS_VALUE = 0
WAPP_PROGRESS_VALUE = 0
WAPP_Driver = None

def load_kv(file_name, file_path=os.path.join("libs", "uix", "kv")):
    """
    `load_kv` func is used to load a .kv file.
    args that you can pass:
        * `file_name`: Name of the kv file.
        * `file_path`: Path to the kv file, it defaults
                       to `project_name/libs/kv`.

    Q: Why a custom `load_kv`?
    A: To avoid some encoding errors.
    """
    with open(os.path.join(file_path, file_name), encoding="utf-8") as kv:
        Builder.load_string(kv.read())
