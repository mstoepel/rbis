import jsonpickle
from uuid import uuid4


class BaseObject(object):
    """
    Provides helpful classes for every class in the game
    """
    def __init__(self):
        pass
        # self.id = uuid4().hex

    def dump(self):
        return jsonpickle.dumps(self, unpicklable=True, keys=True, numeric_keys=True, make_refs=True)

    @staticmethod
    def load(data):
        return jsonpickle.loads(data)
