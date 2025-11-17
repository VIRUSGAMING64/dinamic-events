import os
from modules.calendar import Calendar
import sys
sys.setrecursionlimit(2**30)
"""
Global variables shared across modules.
"""
try:
    os.mkdir("saved")
except:
    pass

calendar = Calendar()
calendar._load_resources('./templates/resources.json')
calendar._load_tasks("./templates/tasks.json")

FONT_SIZE = ...