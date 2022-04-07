import json
from MyEncoder import myEncoder

class ExerciseCollection:
    def __init__(self, exercises):
        # self.type = exercises
        self.exercises = exercises

    def __iter__(self):
        yield from {
            "exercises": self.exercises
        }.items()
    
    def __str__(self):
        return json.dumps(dict(self), cls=myEncoder, ensure_ascii=False)

    def __repr__(self):
        return self.__str__()
    
    def to_json(self):
        return self.__str__()

