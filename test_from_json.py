import json
from dataclasses import dataclass
from typing import List

from packages.JsonSerializeClass import JSC


@dataclass
class Www(JSC):
    i: int
    j: int

@dataclass
class Qqq(JSC):
    x: int
    y: str
    z: int

@dataclass
class Config(JSC):
    aaa: Qqq
    bbb: Qqq
    ccc: List[Www]

if __name__ == "__main__":
    with open("config.json", "r") as fin:
        config: Config = Config.from_json(json.load(fin))
        print(config)
