import json

def load(fileName):
    file = open(f".\\data\\{fileName}.json", "r")
    data = json.loads( file.read())
    file.close()
    return data

def save(fileName, data):
    file = open(f".\\data\\{fileName}.json", "r")
    file.write(json.dumps(data))
    file.close()
