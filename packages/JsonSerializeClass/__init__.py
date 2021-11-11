import json
import re
import sys
from inspect import signature


__all__ = ["JSC"]

rex = re.compile(r"\((.*?)\)")

def get_class(className: str):
    names = className.split(".")
    cls = sys.modules[names[0]]
    for name in names[1:]:
        cls = getattr(cls, name)
    return cls

def get_attr(className: str, value):
    if className in ["int", "float", "str"]:
        return value

    if className.startswith("List"):
        cls = get_class(className[5: -1])
        return [cls.from_json(v) for v in value]

    return get_class(className).from_json(value)

class JSC:
    def to_dict(self):
        d = self.__dict__
        for attr in d:
            if "to_dict" in dir(d[attr]):
                d[attr] = d[attr].to_dict()
        return d

    def to_json(self):
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, data):
        args = rex.search(str(signature(cls))).group(1).split(", ")
        return cls(**{
            attr: get_attr(className, data[attr])
            for attr, className
            in [arg.split(": ") for arg in args]
        })
