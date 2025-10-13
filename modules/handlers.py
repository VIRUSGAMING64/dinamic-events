import json
import datetime


class BasicHandler:
    aviable_tasks = {}
    currents_tasks = []
    resources = {}
    used_resources = {}
    chunk_size = 65535
    def _load_json(self,filename):
        if self._ex_ext(filename) != 'json':
            raise Exception("need a json file")
        data = ''
        tmp = open(filename,'r')
        line = tmp.read(self.chunk_size)
        while line != '':
            data = data + line
            line = tmp.read(self.chunk_size)
        data = self._jsonstr_to_dict(data)
        return data

    def _load_resources(self,filename):
        data = self._load_json(filename)
        self.resources = data
    
    def _ex_ext(self,filename):
        #extract extension function
        filename = filename.split('.')
        return filename[-1] #this works (readed in docs.python.org)
    
    def _jsonstr_to_dict(self,json_data):
        return json.loads(json_data)

    def _dict_to_jsonstr(self,dict_data):
        return json.dumps(dict_data)

    def _load_tasks(self,name):
        data = self._load_json(name)
        self.aviable_tasks = data

class event(BasicHandler):    
    next = None
    start = 0
    end = 0
    def __init__(self,_json:dict):
        self.need_resources:list = _json["resources"]
        self.date = _json["date-range"]
        self.time:list = _json['time-range'] #enter in minute that start
        self.start = int(self.time[0])
        self.end = int(self.time[1])
        self.task:str = _json['name']
        self._load_resources("resources.json")
        A = set()
        for x in self.need_resources:
            A.add(x)
        for x in self.need_resources:
            needed = self.get_sources_dependency(x)
            for x in needed:
                A.add(x)

        B = set()
        for x in A:
            for el in self.resources[x]["without"]:
                B.add(el)

        Colisions = A & B
        if len(Colisions) > 0:
            raise BaseException("invalid task, exist colision")

    def get_sources_dependency(self,res:str,vis = {}):
        try:
            if vis[res] == 1:return []
        except:
            vis[res] = 1
            #not visited
            pass
        neds = []
        for x in self.resources[res]["need"]:
            neds.append(x)
            neds += self.get_sources_dependency(res)
        return neds

    def get_no_utilization(self,res:str):
        noneds = []
        for x in self.resources[res]["whitout"]:
            noneds.append(x)
        return noneds
    
class Calendar(BasicHandler):
    currents_event = None # current event 
    next_events = [] # contanins events in order 
    def __init__(self):
        pass

    def cancel_current(self):
        tmp=self.currents_event
        self.currents_event = self.next_event()
        return tmp

    def save_json_datas(self,calendar_name = 'calendar.json'):
        try:
            save_res = self._dict_to_jsonstr(self.resources)
            save_Ures = self._dict_to_jsonstr(self.used_resources)
            fi = open('resources.json',"w")
            fi.write(save_res)
            fi.close()
            fi = open('used_resources.json',"w")
            fi.write(save_Ures)
            fi.close()
            data = "in progress"
            fi = open(calendar_name,"w")
            fi.write(data)
            fi.close()
        except Exception as e:
            print("maybe you don't have access to this file: ",e)

    def create_task(self,start:int,end:int,taskname:str,daterange:list):
        task = event({
            "name":taskname,
            "time-range":[start,end],
            "resources":self.aviable_tasks[taskname]['need'],
            "date-range":daterange
        })
        return task

    def next_event(self):
        pass
    
    def add_event(self,new:event):
        """
        optimizar esto
        si da tiempo
        """
        try:
            dt = new.start
            while (dt <= new.end):
                for resource in new.need_resources:
                    res = 0
                    try:
                        res = self.used_resources[dt][resource]
                    except:
                        try:
                            res = self.used_resources[dt]
                            self.used_resources[dt][resource] = 0    
                        except:
                            self.used_resources[dt] = {}
                            self.used_resources[dt][resource] = 0
                        finally:
                            res = 0
                    if (res >= self.resources[resource]["count"]):
                        return 0
                dt+=1
            self.currents_tasks.append(new)
            dt = new.start
            while (dt <= new.end):
                for resource in new.need_resources:
                    self.used_resources[dt][resource]+=1
                dt+=1

            return 1
        
        except Exception as e:
            print("unknow exception: ",e)
    
    def remove_event(self,id):
        pass

    def findlasterr(self,new:event):
        try:
            lasterr = 0
            dt = new.start
            while (dt <= new.end):
                for resource in new.need_resources:
                    res = 0
                    try:
                        res = self.used_resources[dt][resource]
                    except:
                        try:
                            res = self.used_resources[dt]
                            self.used_resources[dt][resource] = 0    
                        except:
                            self.used_resources[dt] = {}
                            self.used_resources[dt][resource] = 0
                        finally:
                            res = 0
                    if (res >= self.resources[resource]["count"]):
                        lasterr = dt
                dt+=1
            return lasterr
        except:
            pass


