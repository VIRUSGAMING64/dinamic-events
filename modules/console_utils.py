import os
import signal
import time 
from modules.gvar import *
from modules.utils import *

def void():
    pass

def _show_events():
    clear_console()
    if debug:
        print(calendar.aviable_tasks)
    print("AVIABLE EVENTS:")
    l = 1
    for i in calendar.aviable_tasks:
        print(f"[{l}] -",i)
        l+=1
    input('\nenter any key to continue...')
def _come_back():
    global LOCATION
    LOCATION = parent[LOCATION]

def _add_event_show_menu():
    global LOCATION,ADD_EVENT_MENU
    LOCATION = ADD_EVENT_MENU
    menu = """
    *****************************
    *      ADD EVENT PANEL      *
    * [1] - Show aviable tasks  * 
    * [2] - Set new             *
    * [3] - Exit                *
    *                           *
    *****************************
    >>> """
    print(menu,end='')

def _add_event():
    pass

def _show_console_resources():
    clear_console()
    if debug:
        print("DEBUGING SHOW_CONSOLE_RESOURCES....")
        print(calendar.resources)
        time.sleep(1)
    print('AVAILABLE RESOURCES')
    idx = 1
    for i in calendar.resources:
        print(f"[{idx}] - ",i, f" count: {calendar.resources[i]['count']}")
        idx+-1
    input('Enter any key to continue...\n')
   
def _show_console_menu():
    menu = """
    ************************************
    *          DINAMIC EVENTS          *
    * [1] - show current calendar      *
    * [2] - show aviable resources     *
    * [3] - add event to calendar      *
    * [4] - remove event from calendar *
    ************************************
    >>> """
    print(menu,end='')

def clear_console():
    #optimizar
    o = os.system('clear')
    
def main_console_loop():
    global MENUS,LOCATION
    while True:
        try:
            clear_console()
            MENUS[LOCATION]()
            imp = get_number(1,MAX_OPTION)
            if imp == None: continue
            MENU_TO[LOCATION][imp]()
        except Exception as e:
            print(e)
            input()

MENU_TO = {
    MAIN_MENU :{    
        1: {},
        2: _show_console_resources,
        3: _add_event_show_menu,
        4: {},
        5: {},
        None: void
    },
    ADD_EVENT_MENU: {
        1:_show_events,
        2:_add_event,
        3:_come_back
    }
}
parent = {
    1:0,
    0:0,
}

MENUS = [
    _show_console_menu,
    _add_event_show_menu,
]
