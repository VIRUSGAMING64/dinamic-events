import os
from modules.calendar import Calendar
import sys
sys.setrecursionlimit(2**30)
"""
THI IS GLOBAL VAR MODULES TO 
SAVE VARIABLE THAT I NEED SHARE 
BETWEEN MODULES
"""
try:
    os.mkdir("saved")
except:
    pass

debug = True
calendar = Calendar()
calendar._load_resources('./templates/resources.json')
calendar._load_tasks("./templates/tasks.json")
MAX_OPTION = 4
LOCATION = 0
FONT_SIZE = ...
##############################
# MENUES
MAIN_MENU = 0
ADD_EVENT_MENU = 1
LOAD_TASK_MENU = 2
JSON_EXAMPLE = '''[
    {
        "name": name_of_task,
        "time": [from,to] | -1
    }
]'''