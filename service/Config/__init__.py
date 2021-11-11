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
