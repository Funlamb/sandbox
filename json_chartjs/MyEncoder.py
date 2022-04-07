from json import JSONEncoder

class myEncoder(JSONEncoder):
    def default(self, obj):
        return obj.__dict__