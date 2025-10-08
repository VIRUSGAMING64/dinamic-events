import json
from modules.gvar import *
import time
import os

def void():
    pass

def get_saved_json(filename):
    jsonstr = read_file(filename)
    return json.load(jsonstr)

def read_file(name):
    task = open(name)
    data = task.read(2**31)
    task.close()
    return data

def clear_console(): #optimizar
    o = os.system('clear')

def get_number(a,b):
    imp = input() # remplace this with getchr to read number task or other or signals to get -> to change
    if imp == '': return None
    num_err = False
    if debug:
        print(f"[debug][imp] {imp}:{type(imp)}")
        time.sleep(1)
    if not imp.isnumeric(): #not number introduced
        num_err  = True
    elif int(imp) < a or int(imp) > b: #option out of range
        num_err = True
    else: #is valid option
        imp = int(imp)
    if num_err:
        print(f'[!] Please enter a valid number in a range [{a},{b}]')
        time.sleep(3)
        return None
    return imp

def get_str():
    string=""
    while string == "":
        string = input(">>> ")
    return string