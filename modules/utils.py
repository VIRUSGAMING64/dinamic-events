import json
from modules.gvar import *
import time
import os
from datetime import datetime

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
        datetime.fromisoformat(date)
        return 1
    except ValueError:
        return 0


def get_saved_json(filename):
    jsonstr = read_file(filename)
    return json.load(jsonstr)


def read_file(name):
    with open(name,'r') as task:
        data = task.read(2**31)
        task.close()
    return data


def tominute(date: datetime | str) -> int:  #TODO
    if isinstance(date, str):
        date = datetime.fromisoformat(date)
    epoch = datetime(1000, 1, 1)
    delta = date - epoch
    return int(delta.total_seconds() // 60)


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