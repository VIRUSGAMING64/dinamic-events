class event():
    def __init__(self,task:dict):
        self.resources:dict = task["resources"]
        self.time:tuple = task['time-range']
        self.task:str = task['name']
        