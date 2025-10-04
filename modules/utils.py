import json

def get_saved_json(filename):
    jsonstr = read_file(filename)
    return json.load(jsonstr)

def read_file(name):
    task = open(name)
    data = task.read(2**31)
    task.close()
    return data

