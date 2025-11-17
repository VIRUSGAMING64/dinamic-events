import json
from modules.gvar import *
import time
import os
from datetime import datetime
import time

def log(*data):
    print(f"[{time.ctime()}]: ",*data,file=(open("logs.txt","a")))

def get_sources_dependency(resources, res: str, visited=None):
    if visited is None:
        visited = set()
    if res in visited:
        return []
    visited.add(res)
    needs = []
    for dependency in resources[res]["need"]:
        needs.append(dependency)
        needs += get_sources_dependency(resources, dependency, visited)
    return needs


def CheckISODate(date:str): 
    try:
        print(date)
        date = date.split("-")
        year = int(date[0])
        mo = int(date[1])
        print(year,mo)
        if int(mo) > 12 or int(mo) <= 0:
            return 0
        d_h = date[2].split("T")
        h = d_h[1]
        d = int(d_h[0])
        h = h.split(':')
        print(h,d,mo,year)
        if int(h[0]) >= 24 or int(h[0]) < 0:
            return 0
        if int(h[1]) >= 60 or int(h[1]) < 0:
            return 0       
        d31 = [1,3,5,7,8,10,12]
        d28 = [2]
        d30 = [4,6,9,11]
        if d <= 0:
            return 0
        if mo == 2 and d > 28:
            return 0
        if mo in d31 and d > 31:
            return 0
        if mo in d30 and d > 30:
            return 0        
        return 1
    except Exception as e:
        log(f"error checking ISO date [{e}]")
        return 0


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
    imp = input() # replace this with getchr to read number task or other or signals to get -> to change
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



def add_to_dict(dic:dict,lis):
    if len(lis) == 2:
        try:
            dic[str(lis[0])] += lis[1]
        except:
            dic[str(lis[0])] = lis[1]
        return
    
    if lis[0] in dic.keys():
        add_to_dict(dic[str(lis[0])],lis[1:])
    else:
        dic[str(lis[0])] = {}
        add_to_dict(dic[str(lis[0])],lis[1:])