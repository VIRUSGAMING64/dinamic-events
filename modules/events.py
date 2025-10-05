class event():    
    next = None
    start = None
    end = None
    def __init__(self,task:dict):
        self.resources:dict = task["resources"]
        self.time:list = task['time-range']
        self.start = self.time[0]
        self.end = self.time[1]
        self.task:str = task['name']
        self.need:list = task["need"]

    def check_sources(self):
        need = self.need.copy()
        disp = self.resources.copy()
        for res in need:
            if disp[res['name']]["count"] - res["count"] <= 0:
                return False
        return 1
    
    