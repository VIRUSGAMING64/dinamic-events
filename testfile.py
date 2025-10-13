import time
import os
from multiprocessing import Process
from typing import *

start = time.time_ns() / 10**9
from modules import *
end = time.time_ns() / 10**9

Time_s = end-start
print(f"IMPORT TIME ELAPSED\n{Time_s} SECONDS")
mtx = False

def single_core_speed(core = 0):
    global mtx
    start = time.time_ns() / 10**9
    x = 0
    for i  in range(10**8):
        x += 0.5
    end = time.time_ns() / 10**9
    Time_s = end-start
    flops = 10**8//Time_s
    i = 0
    id = ["","K","M","G","T","Y"]
    while flops // 1000 >= 1:
        flops /= 1000
        i+=1
    while mtx == True: time.sleep(311/10000)
    mtx = True
    print(f"CORE {core} SPEED TEST\npython speed 1e8 Floting Points Operations in {Time_s}s\n{id[i]}flops: {flops}".upper())
    mtx = False
cores = os.cpu_count()
def cores_speed():
    for i in range(cores):
        Process(args=[i],target=single_core_speed).start()

print("==============================================")
print("==============================================")
print('now in ctime:',tominute(datetime.now()))
print('now in ctime:',tominute(datetime(1,1,2,0,10)))
print("==============================================")
print("==============================================")

da=datetime.now()
s=tominute(da)
da2 =da.replace(year=da.year+1)
e=tominute(da2)

ev = event(
    {
        "name": "mine btc",
        "time-range":[s,e],
        "resources": ['cpu'],
        "date-range": [da,da2]
    }
)

print("dependency:",ev.get_sources_dependency("ram"))

print("==============================================")
print("==============TEST ADD EVENT==================")
start = time.time_ns() / 10**9
da=calendar.add_event(ev)
print("aded",da)
da=calendar.add_event(ev)
print('aded',da)
end = time.time_ns() / 10**9
Time_s = end-start
print(f"ADDING TIME ELAPSED\n{Time_s} SECONDS")
print("==============================================")
print("==============TEST RESOURCES==================")
print(calendar.resources)
print("==============TESTING SAVE====================")
start = time.time_ns() / 10**9
calendar.save_json_datas("testcalendar.json")
end = time.time_ns() / 10**9
Time_s = end-start
print(f"SAVING TIME ELAPSED\n{Time_s} SECONDS")
print("==============================================")
print("==============TEST LAST ERROR=================")
print("last index error: ",calendar.findlasterr(ev),"init: ",ev.start,"end: ",ev.end)
print("==============TEST LAST ERROR=================")



#cores_speed()
