from modules.handlers import Calendar
import sys
sys.setrecursionlimit(2**30)
"""
THI IS GLOBAL VAR MODULES TO 
SAVE VARIABLE THAT I NEED SHARE 
BETWEEN MODULES
"""

debug = True
calendar = Calendar()
calendar._load_resources('resources.json')
calendar._load_tasks("tasks.json")
MAX_OPTION = 4
LOCATION = 0
MAIN_MENU = 0
ADD_EVENT_MENU = 1