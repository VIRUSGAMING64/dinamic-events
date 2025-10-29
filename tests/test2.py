import datetime
from modules.gvar import *
from modules.calendar import *
from modules.utils import tominute
print("||||||||||||||||||||||||||||||||||||||||||||||||")
import time
start = time.time_ns()
print("STRESS TEST")

L = datetime.datetime.now()
dt = datetime.timedelta(days=1)
R = L + dt


total = 3650
for i in range(365 * 10):
    ev = event({
        "date-range":[L.isoformat(),R.isoformat()],
        'time-range':[tominute(L),tominute(R)],
        "name": "mine btc",
        "resources": ["cpu"],
        "notes":"testing"
    })
    L = L + dt
    R = L + dt
    calendar.add_event(ev)


print("saving")
calendar.save_json_datas()
print("saved")








end = time.time_ns()
elapsed = (end-start)/10**9
print(elapsed,"s",sep="")