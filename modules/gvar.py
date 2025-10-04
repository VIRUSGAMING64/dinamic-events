from modules.handlers import Calendar
"""
THI IS GLOBAL VAR MODULES TO 
SAVE VARIABLE THAT I NEED SHARE 
BETWEEN MODULES
"""

debug = True
calendar = Calendar()
calendar._load_resources('resources.json')
MAX_OPTION = 4
LOCATION = 0
MAIN_MENU = 0
ADD_EVENT_MENU = 1