from modules import *
begin = time.time_ns()
print("begin stress test 2")
cal = Calendar("t_used.json","t_actives.json")
cal._load_resources('./templates/resources.json')
cal._load_tasks("./templates/tasks.json")
print(cal.resources)
cal.remove_old_events()

def timer(func,*args):
    s=time.time_ns()
    out = func(*args)
    e=time.time_ns()
    return out , e - s

l = datetime.datetime.now()
r = l + datetime.timedelta(1)
c = 0
trr = 0
prom = 0

for i in range(1000):
    trr+=1
    l += datetime.timedelta(2)
    r += datetime.timedelta(2)
    tl = tominute(l)
    tr = tominute(r)
    new = event(
        {
            "name": "test",
            "notas": "para hacer test",
            "date-range": [l.isoformat(),r.isoformat()],
            "time-range": [tl,tr],
            "resources": ["cpu"]
        }  
    )
    add,el=timer(cal.add_event,new)
    prom += el
    if add == True:
        c+=1

end = time.time_ns()
cal.save_json_data()
elapsed = (end - begin) / 10**9


print(elapsed,f"media of add function time (ms): {(el / trr) / 10**6}", "total events: ",trr,"addeds: ", c, "real_added: ", len(cal.events))