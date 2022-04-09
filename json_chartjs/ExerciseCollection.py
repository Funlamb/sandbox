import json
from MyEncoder import myEncoder

class ExerciseCollection:
    def __init__(self, exercises):
        self.version = 1
        self.exertest = exercises

    def __iter__(self):
        yield from {
            "version": 1,
            "type": self.exertest
        }.items()
    
    def __str__(self):
        return json.dumps(dict(self), cls=myEncoder, ensure_ascii=False)

    def __repr__(self):
        return self.__str__()
    
    def to_json(self):
        print("to_json")
        to_return = {"version": self.version}
        exercises = {}
        for key, exer in self.exertest.item():
            jexer = []
            for j in exer:
                jexer.append(j.__dict__)
            exercises[key] = jexer
        to_return["return"] = exercises
        return self.__str__()

