from modules.events import *
from modules.SegTree import *
from modules.Pool import *

class Calendar(BasicHandler):
    used_resources:dict = {}
    available_tasks:dict = {}
    events:list[event] = []
    inqueue:dict[event,bool] = {} 
    
    def __init__(self,used_res = "used_resources.json", actives_ev = "actives_events.json"):
        try:
            self.actives_events_path = actives_ev
            self.used_res_path = used_res
            self.load_used_resources(f"{SAVE_ROOT}/{used_res}")
            ex = self._load_json(f"{SAVE_ROOT}/{actives_ev}")
            self.events = []
            for i in ex:
                self.events.append(event(i))
            self.save_json_data()
        except Exception as e:
            log(f"error loading used resources: ",e)
            pass
    def is_running(self,ev):
        return self.inqueue.get(ev, False)

    def list_events(self): 
        return self.events

    def load_used_resources(self, filename):
        self.used_resources = self._load_json(filename)

    def save_json_data(self):
        sv = []
        for ev in self.events:
            sv.append(ev.__dict__())
        fi = open(f"{SAVE_ROOT}/{self.actives_events_path}","w")
        fi.write(json.dumps(sv,indent=3))
        fi.close()
        try:
            save_used_resources = self._dict_to_jsonstr(self.used_resources)
            fi = open(f'{SAVE_ROOT}/{self.used_res_path}',"w")
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
    def gen_tree(self, l , length):
        
        id = 0
        a2 = [l,l + length]
        di = {}
        for i in self.events:
            x = int(i.start)
            a2.append(x)
            x = int(i.end)
            a2.append(x)
            a2.append(i.end + 1)
    
        a2.sort()
    
        for x in a2:
            if di.get(x,-1) == -1:
                di[x] = id
                id += 1 
        tree = SegTree([0] * (id + 10) )
        
        for x in self.events:
            l = di[x.start]
            r = di[x.end]
            tree.update(l,r,1)
                    
        
        return di,tree
    
    def check_available(self, new_res: str, start: int, end: int, di , tree):
        if not (new_res in self.used_resources.keys()):
            return True
        try:
            
            l = di[start]
            r = di[end]
            mx = tree.query(l,r)
            if mx >= self.resources[new_res]["count"]:
                return False
                
        except Exception as e:
            log("error checking available resource: ", str(e))
            return False
            
        return True
        
    def add_event(self,new:event):
        self.sort()
        di,tree = self.gen_tree(new.start,new.end - new.start)
        try:
            for res in new.need_resources:
                av = self.check_available(res, new.start, new.end, di, tree)
                if av == False:
                    return av
            self.events.append(new)
            self.inqueue[new] = True

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
        del self.inqueue[deleted]

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
        self.events  = []
        for x in events:
            self.add_event(x)

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

    def suggest_brute_lr(self, L: int, R: int, resources: list):
        length = (R-L)
        print(type(L),type(R))
        l = tominute(datetime.datetime.now())
        start = datetime.datetime.now()
        
        self.sort()
        
        di,tree = self.gen_tree(l,length)
    
        for res in resources:
            while not self.check_available(res, l, l + length, di , tree):
                mx:int = 2**300
                for x in self.list_events():
                    if (l < x.end) and (l >= x.start):
                        mx = min(mx, x.end+1)
                if mx == 2**300:
                    mx = l + 1
                ant:int = l
                l:int = mx
                dif:int = l - ant
                dr = datetime.timedelta(minutes=dif)
                start+=dr

        return start
    
