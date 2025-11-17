from modules.events import *
from modules.SegTree import *

class Calendar(BasicHandler):
    used_resources = {}
    available_tasks = {}
    current_tasks = []
    current_event = None  # current event
    events = []
    
    def __init__(self):
        try:
            self.load_used_resources(f"{SAVE_ROOT}/used_resources.json")
            ex = self._load_json(f"{SAVE_ROOT}/actives_events.json")
            self.events = []
            for i in ex:
                self.events.append(event(i))
            self.remove_old_events()
            self.save_json_data()
        except Exception as e:
            # error loading data
            log(f"error loading used resources: ",e)
            pass
    
    def list_events(self):  # definitivamente no se puede optimizar
        self.remove_old_events()
        return self.events

    def load_used_resources(self, filename):
        self.used_resources = self._load_json(filename)

    def save_json_data(self):
        sv = []
        for ev in self.events:
            sv.append(ev.__dict__())
        fi = open(f"{SAVE_ROOT}/actives_events.json","w")
        fi.write(json.dumps(sv,indent=3))
        fi.close()
        try:
            save_used_resources = self._dict_to_jsonstr(self.used_resources)
            fi = open(f'{SAVE_ROOT}/used_resources.json',"w")
            fi.write(save_used_resources)
            fi.close()
        except Exception as e:
            print("maybe you don't have access to this file: ",e)

    def create_task(self,start:int,end:int,taskname:str,daterange:list):
        try:
            task = event({
                "name":taskname,
                "time-range":[start,end],
                "resources": [],
                "date-range":daterange
            })
        except Exception as e:
            log("error creating task",e)
            return None
        try:
            for elem in self.available_tasks[taskname]["resources"]:
                task.need_resources.append(elem['name'])
        except Exception as e:
            print("error adding resources to task: ",e)
            input()
            return None
        return task
    
    def check_available(self, new_res: str, start: int, end: int):
        if not (new_res in self.used_resources.keys()):
            return True
        
        self.sort()
        
        for res in self.used_resources:
            if res != new_res:
                continue
            try:
                sum = 0
                id = 0
                a2 = [start,end]
                a = [0] * (id + 10)
                di = {}

                for i in self.events:
                    x = int(i.start)
                    a2.append(x)
                    x = int(i.end)
                    a2.append(x)
                
                a2.sort()

                for x in a2:
                    if di.get(x,-1) == -1:
                        di[x] = id
                        id += 1  

                ##* hasta aqui hice la comprecion de coordenadas

                tree = SegTree(a)
                
                for x in self.events:
                    l = di[x.start]
                    r = di[x.end]
                    tree.update(l,r,1)
                               
                l = di[start]
                r = di[end]
                mx = tree.query(l,r)

                if mx >= self.resources[res]["count"]:
                    print("here = ", f"[{mx},{l},{r}]     {a} ,  {a2}")
                    return False
                
            except Exception as e:
                log("error checking available resource: ", e)
                return False
        return True
        
    def add_event(self,new:event):
        """
        optimizar esto si da tiempo
        """
        self.sort()
        self.remove_old_events()
        try:
            for res in new.need_resources:
                av = self.check_available(res, new.start, new.end)
                if av == False:
                    return av
            self.events.append(new)
            for res in new.need_resources:     
                add_to_dict(self.used_resources,[res,new.start,1])        
                add_to_dict(self.used_resources,[res,new.end,-1])
            return True
        except Exception as e:
            log("error adding event: [unknown error]", e)
        return False

    def remove(self,index):
        deleted = self.events.pop(index)
        for res in deleted.need_resources:
            add_to_dict(self.used_resources,[res,deleted.start, -1])
            add_to_dict(self.used_resources,[res,deleted.end, 1])
        self.remove_old_events()

    def _no_check_add(self,events:list[event]):
        try:
            for ev in events:
                for res in ev.need_resources:
                    add_to_dict(self.used_resources,[res,ev.start, 1])
                    add_to_dict(self.used_resources,[res,ev.end, -1])
        except Exception as e:
            log(f"error adding without check [{e}]")

    def remove_old_events(self):
        self.sort()
        now = datetime.datetime.now()
        init_t = tominute(now)
        del now
        events = []
        for task in self.events:
            if init_t < task.end:
                events.append(task)
        self.used_resources = {}
        self.events = events
        self._no_check_add(events)

    def sort(self):
        """
        this function sort keys of self.used_resources by age
        """
        temp = {}
        for res in self.used_resources:
            temp[res] = {}
            keys = list(map(int,self.used_resources[res].keys()))
            keys.sort()
            for key in keys:
                temp[res][str(key)] = self.used_resources[res][str(key)]

            for key in keys:
                self.used_resources[res][str(key)] = temp[res][str(key)]
        self.used_resources = {}
        for res in temp:
            self.used_resources[res] = temp[res]

    def suggest_brute(self, ev: event):
        """
    Return minimum position to add event.
    How to optimize?
    Consider inter-task binding and current time first.
        """
        length = ev.end - ev.start
        l = tominute(datetime.datetime.now())
        for res in ev.need_resources:
            while not self.check_available(res, l, l + length):
                l+=1
        return l

    def suggest_brute_lr(self, L: int, R: int, resources: list):
        """
        Return minimum position to add event.
        How to optimize?
        Consider inter-task binding and current time first.
        """

        length = (R-L)
        print(type(L),type(R))
        l = tominute(datetime.datetime.now())
        start = datetime.datetime.now()
        LR = []

        for res in resources:
            print(type(l),type(length), l, start.isoformat(" "))
            
            while not self.check_available(res, l, l + length):
                mx = 2**300

                print(start.isoformat(),l,self.events[0].start,self.events[0].end, length)

                for x in self.list_events():
                    if (l < x.end) and (l >= x.start):
                        mx = min(mx, x.end)

                if mx == 2**300:
                    mx = l + 1
                
                ant = l
                l = mx - 1
                l+=1
                dif = l - ant
                dr = datetime.timedelta(minutes=dif)
                start+=dr

        return start
    
