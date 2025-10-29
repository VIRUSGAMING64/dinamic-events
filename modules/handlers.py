import json
from modules.gvar import *
from modules.utils import *
import datetime
import modules.filelogin as log
SAVE_ROOT = "./saved"

class BasicHandler:
    resources = {}
    chunk_size = 65535
    def _load_json(self,filename):
        filename = os.path.realpath(filename)
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
        filename = os.path.realpath(filename)
        data = self._load_json(filename)
        self.resources = data
    
    def _ex_ext(self,filename):
        filename = os.path.realpath(filename)
        #extract extension function
        filename = filename.split('.')
        return filename[-1] #this works (readed in docs.python.org)
    
    def _jsonstr_to_dict(self,json_data) -> dict:
        return json.loads(json_data)

    def _dict_to_jsonstr(self,dict_data):
        return json.dumps(dict_data,indent=3)

    def _load_tasks(self,name):
        filename = os.path.realpath(name)
        data = self._load_json(name)
        self.aviable_tasks = data
