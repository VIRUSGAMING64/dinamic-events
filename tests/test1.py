import time
start = time.time_ns() / 10**9
import os
from modules.events import *
from multiprocessing import Process
from typing import *
import datetime as dt
from modules.utils import *
from modules.gvar import *
from datetime import datetime
import os

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

#cores_speed()

print('now in ctime:',tominute(datetime.now()))
print('now in ctime:',tominute(datetime(1,1,2,0,10)))

da=datetime.now()
s=tominute(da)
dl=dt.timedelta(minutes=1)
da2 = da+dl
e=tominute(da2)

ev = event(
    {
        "name": "mine btc",
        "time-range":[s,e],
        "resources": ['cpu'],
        "date-range": [da.isoformat(),da2.isoformat()]
    }
)

print("dependency:",get_sources_dependency(calendar.resources,"ram"))
print("==============TEST ADD EVENT==================")

start = time.time_ns() / 10**9
da=calendar.add_event(ev)
print("aded",da)
ev.end += 10
da=calendar.add_event(ev)
print('aded',da)
end = time.time_ns() / 10**9
Time_s = end-start

print(f"ADDING TIME ELAPSED\n{Time_s} SECONDS")
print("==============TEST RESOURCES==================")
print(calendar.resources)
print("==============TESTING SAVE====================")

start = time.time_ns() / 10**9
calendar.save_json_datas()
end = time.time_ns() / 10**9
Time_s = end-start

print(f"SAVING TIME ELAPSED\n{Time_s} SECONDS")
print("==============TEST LAST ERROR=================")
#print("last index error: ",calendar.findlasterr(ev),"init: ",ev.start,"end: ",ev.end)


    