import json
from modules.gvar import *
import time
import os
from datetime import datetime

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

def tominute(date:datetime):
    minute = date.minute
    minute += (date.hour) * 60 
    minute += (date.day-1) * 24 * 60
    mon = date.month - 1 
    ye = date.year - 1
    ye = ye * 365 + int(ye // 4)
    ye = ye * 24 * 60
    mon = dict({
        0:0,
        1:31,
        2:31+28 +((date.year % 4 )== 0),
        3:31+28 +((date.year % 4 )== 0) + 31,
        4:31+28 +((date.year % 4 )== 0) + 31 + 30,
        5:31+28 +((date.year % 4 )== 0) + 31 + 30 + 31,
        6:31+28 +((date.year % 4 )== 0) + 31 + 30 + 31 + 30,
        7:31+28 +((date.year % 4 )== 0) + 31 + 30 + 31 + 30 + 31,
        8:31+28 +((date.year % 4 )== 0) + 31 + 30 + 31 + 30 + 31 + 31,
        9:31+28 +((date.year % 4 )== 0) + 31 + 30 + 31 + 30 + 31 + 31 + 30,
        10:31+28 +((date.year % 4 )== 0) + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31,
        11:31+28 +((date.year % 4 )== 0) + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31 + 30,
    })[mon]
    minute += ye
    minute += mon * 24 * 60
    return minute
