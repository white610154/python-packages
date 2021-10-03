import json


class JSC:
    def to_dict(self):
        d = self.__dict__
        d.update({
            attr: d[attr].toDict()
            for attr in d
            if 'toDict' in dir(d[attr])
            })
        return d

    def to_json(self):
        return json.dumps(self.toDict())
