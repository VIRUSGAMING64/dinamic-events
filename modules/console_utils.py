
import time 
from modules.gvar import *
from modules.utils import *

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


def _get_file_content():
    print(f"please enter filename\nthe file is json with a format:\n{JSON_EXAMPLE}")
    name = get_str()
    data = None
    try:
        with open(name) as file:
            data = file.read(2**30)
            file.close()
        if data == None:
            print("no loaded :'(\n")
        else:
            print("loaded !!!")
    except Exception as e:
            print(e)
            input('error :[')
    finally:
        input('press any key to continue...')
    return data

def _come_back():
    global LOCATION,MAX_OPTION
    LOCATION = parent[LOCATION]
    MAX_OPTION = sizes[LOCATION]


def _add_event_show_menu():
    global LOCATION,ADD_EVENT_MENU,MAX_OPTION
    LOCATION = ADD_EVENT_MENU
    MAX_OPTION = 3
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
    global LOCATION,MAX_OPTION
    LOCATION = LOAD_TASK_MENU
    MAX_OPTION = 3
    
def _add_task_meno_how_to():

    menu = """
    *****************************
    *      LOAD EVENT PANEL     *
    * [1] - Generate            * 
    * [2] - open from files     *
    * [3] - Exit                *
    *                           *
    *****************************
    >>> """
    print(menu,end='')


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
        idx+=1
    input('Enter any key to continue...\n')
   
def _show_console_menu():
    global MAX_OPTION
    MAX_OPTION = 5
    menu = """
    ************************************
    *          DINAMIC EVENTS          *
    * [1] - show current calendar      *
    * [2] - show aviable resources     *
    * [3] - add event to calendar      *
    * [4] - remove event from calendar *
    * [5] - save currents tasks        *
    ************************************
    >>> """
    print(menu,end='')    

def main_console_loop():
    global MENUS,LOCATION,MAX_OPTION
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



def _load_from_file():
    data = _get_file_content()
    data = calendar._jsonstr_to_dict(data)
    for new_task in data:
        new = calendar.create_task(
            tominute(datetime.fromisoformat(new_task["time"][0])),tominute(datetime.fromisoformat(new_task['time'][1])),
            new_task['name'],new_task["time"]
        )
        calendar.add_event(new)


def _save_calendar():
    clear_console()
    menu ="""
    **************************
    * ENTER FILENAME TO SAVE *
    **************************
"""
    try:
        print(menu)
        get_str()
        calendar.save_json_datas()
        print('DATAS SAVED')
    except Exception as e:
        print(e)
    finally:
        input() 

MENU_TO = {
    MAIN_MENU :{    
        1: void,
        2: _show_console_resources,
        3: _add_event_show_menu,
        4: void,
        5: _save_calendar,
        None: void
    },
    ADD_EVENT_MENU: {
        1:_show_events,
        2:_add_event,
        3:_come_back
    },
    LOAD_TASK_MENU: {
        1:void,
        2:_load_from_file,
        3:_come_back
    }
}

parent = {
    MAIN_MENU:MAIN_MENU,
    ADD_EVENT_MENU:MAIN_MENU,
    LOAD_TASK_MENU:ADD_EVENT_MENU
}

sizes = {
    MAIN_MENU:5,
    ADD_EVENT_MENU:3,
    LOAD_TASK_MENU: 3
}

MENUS = [
    _show_console_menu,
    _add_event_show_menu,
    _add_task_meno_how_to,
]
