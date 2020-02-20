from json import JSONEncoder

class MyEncoder(JSONEncoder):
    def __init__(self, label, time, data, origin, number):
        self.label = label
        self.time = time
        self.values = data
        self.origin = origin
        self.origin = number