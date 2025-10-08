import time
import os
from multiprocessing import Process

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

def cores_speed():
    for i in range(os.cpu_count()):
        Process(args=[i],target=single_core_speed).start()

cores_speed()