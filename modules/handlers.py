import os
import os.path as path
import json
import datetime as date
from modules.events import *

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
        data = self._jsonstr_to_dict(data)
        self.resources = data
        return data


    def _ex_ext(self,filename):
        #extract extension function
        filename = filename.split('.')
        return filename[-1] #this works (readed in docs.python.org)
    
    def _jsonstr_to_dict(self,json_data):
        return json.loads(json_data)

    def _dict_to_jsonstr(self,dict_data):
        return json.dumps(dict_data)

    def save_json_datas(self):
        try:
            save_res = self._dict_to_jsonstr(self.resources)
            save_Ures = self._dict_to_jsonstr(self.used_resources)
            fi = open('resources.json')
            fi.write(save_res)
            fi.close()
            fi = open('used_resources.json')
            fi.write(save_Ures)
            fi.close()
        except Exception as e:
            print("maybe you don't have access to this file: ",e)

        
class Calendar(BasicHandler):
    currents_event = None # current event 
    next_events = [] # contanins events in order 

    def __init__(self,event = None):
        if event == None: return
        self.currents.append(event)
    
    def cancel_current(self):
        self.currents_event = self.next_event()

    def next_event(self):
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
