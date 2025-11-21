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

def get_saved_json(filename):
    jsonstr = read_file(filename)
    return json.load(jsonstr)

def read_file(name):
    task = open(name)
    data = task.read(2**31)
    task.close()
    return data

def tominute(date:datetime):
    return int(date.timestamp()) // 60

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


def event_option_label(idx: int, ev) -> str:
    return f"[{idx}] {ev.task} FROM {ev.date[0]} TO ..."


def build_event_option_labels(events: list) -> list:
    return [event_option_label(idx, ev) for idx, ev in enumerate(events)]


def parse_event_option(option: str):
    if not option or "]" not in option:
        return None
    try:
        prefix = option.split("]", 1)[0]
        prefix = prefix.replace("[", "").strip()
        return int(prefix)
    except ValueError:
        return None


def format_event_info(ev) -> str:
    resources = ', '.join(ev.need_resources) if ev.need_resources else "-"
    lines = [
        "INFORMATION:",
        f"Task name: {ev.task}",
        f"Start Date: {ev.date[0]}",
        f"End Date: {ev.date[1]}",
        f"Time range: {ev.time[0]} TO {ev.time[1]}",
        f"Resources needed: {resources}",
        f"Notes: {ev.notes}",
    ]
    return "\n".join(lines)