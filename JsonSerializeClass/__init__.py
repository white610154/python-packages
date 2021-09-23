import json

class JSC:
    def toDict(self):
        d = self.__dict__
        d.update({
            attr: d[attr].toDict()
            for attr in d
            if 'toDict' in dir(d[attr])
            })
        return d

    def toJson(self):
        return json.dumps(self.toDict())
