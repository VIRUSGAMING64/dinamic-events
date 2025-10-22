import time

def log(*data):
    print(f"[{time.ctime()}]: ",*data,file=(open("logs.txt","a")))