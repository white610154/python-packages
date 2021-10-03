from dataclasses import dataclass

@dataclass
class Aaa(dict):
    x: int
    y: int

a = Aaa(10, 11)
print(a.__dict__)