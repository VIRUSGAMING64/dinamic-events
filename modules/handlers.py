import os
import os.path as path
import json
if __name__ != '__main__':
    from modules.events import *
else:
    from events import *

class BasicHandler:
    resources = {
    
    }
    used_resources = { 

    }
    chunk_size = 65535
    def _load_resources(self,filename):
        if self._ex_ext(filename) != 'json':
            raise "need a json file"
        data = ''
        tmp = open(filename,'r')
        line = tmp.read(self.chunk_size)
        while line != '':
            data = data + line
            line = tmp.read(self.chunk_size)
        json_resources = json.loads(data)
        #combert json_resources to dict
        return json_resources
    
    def _ex_ext(self,filename):
        #extract extension function
        filename = filename.split('.')
        return filename[-1]
    
    def _jsonstr_to_dict(json_data):
        pass

    def _dict_to_jsonstr(dict_data):
        pass

    def save_resources(self,filename):
        pass

class Calendar(BasicHandler):
    currents_event = None
    next_events = []

    def __init__(self,event = None):
        if event == None: return
        self.currents.append(event)
    
    def cancel_current(self):
        pass

    def add_event(self,event):
        pass

    def remove_event(self,id):
        pass

    def change_event(self,id,event):
        pass

    def find(self,id):
        """return first date of {id} task"""
        pass

if __name__ == '__main__':
    print('test mode')
    hand = Calendar()
    print(hand._ex_ext('filename'))
    print(hand._load_resources('resources.json'))