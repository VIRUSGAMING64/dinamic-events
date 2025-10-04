import os
import signal
import time 
from modules.gvar import *

def _show_console_resources():
    if debug:
        print("DEBUGING SHOW_CONSOLE_RESOURCES....")
        print(calendar.resources)
        time.sleep(1)
    print('AVIABLE RESOURCES')
    for i in calendar.resources:
        print(i, f" count: {calendar.resources[i]['count']}")
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
            imp = input() # remplace this with getchr to read number task or other or signals to get -> to change
            if imp == '': continue
            num_err = False
            if debug:
                print(f"[debug][imp] {imp}:{type(imp)}")
                time.sleep(1)
            if not imp.isnumeric(): #not number introduced
                num_err  = True
            elif int(imp) < 1 or int(imp) > MAX_OPTION: #option out of range
                num_err = True
            else: #is valid option
                imp = int(imp)
                if debug:
                    print('[debug] option called....') 
                    time.sleep(1)
                MENU_TO[imp]()
            if num_err:
                print(f'[!] Please enter a valid number in a range [1,{MAX_OPTION}]')
                time.sleep(3)

        except Exception as e:
            print(e)
            input()


MENU_TO = {
    1: 1,
    2: _show_console_resources,
    3: {},
    4: {},
    5: {},
}

MENUS = [
    _show_console_menu,
]
