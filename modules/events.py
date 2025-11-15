from modules.handlers import *

class event(BasicHandler):    
    next = None
    start = 0
    end = 0
    notes = ""
    def __init__(self,_json:dict):
        try:
            self.need_resources:list = _json["resources"]
            self.date = _json["date-range"]
            self.time:list = _json['time-range'] #enter in minute that start
            self.task:str = _json['name']
            if "note" in _json.keys():
                self.notes = _json["note"]
            self.start = int(self.time[0])
            self.end = int(self.time[1])
            
            if self.start > self.end:
                raise Exception("Invalid range [R < L]")
            
            self._load_resources("./templates/resources.json")
            Deps = set()        
            for x in self.need_resources:
                Deps.add(x)
            for x in self.need_resources:
                needed = get_sources_dependency(self.resources,x)
                for x in needed:
                    Deps.add(x)
            NoUse = set()
            for x in Deps:
                for el in self.resources[x]["without"]:
                    NoUse.add(el)
            Colisions = Deps & NoUse
            if len(Colisions) > 0:
                raise BaseException("invalid task, exist colision")
            self.need_resources = list(Deps)
        except Exception as e:
            log(f"error initialicing event [{e}]")

    def __str__(self):
        return json.dumps({
            "time-range": self.time,
            "date-range": self.date,
            "resources" : self.need_resources,
            "name":self.task,
            "notes": self.notes
        })

    def __dict__(self):
        return json.loads(self.__str__())
    
    def get_no_utilization(self,res:str):
        noneds = []
        for x in self.resources[res]["whitout"]:
            noneds.append(x)
        return noneds
