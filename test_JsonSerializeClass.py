from JsonSerializeClass import JSC

class Aaa(JSC):
    '''
    simply inherit JSC(JsonSerializeClass) to add methods: toDict, toJson
    '''
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Bbb:
    '''
    or not to inherit JSC, but implement toDict method to simulate JSC
    '''
    def __init__(self, x, y, z):
        self.a = Aaa(x, y)
        self.z = z

    def toDict(self):
        return {
            'a': self.a.x + self.a.y,
            'z': self.z,
        }

class Ccc(JSC):
    '''
    create an object to show how this package works
    '''
    def __init__(self, w, x, y ,z):
        self.w = w
        self.a = Aaa(x, y)
        self.b = Bbb(x, y, z)

if __name__ == '__main__':
    # this will recursively turn object to dictionary
    print(Ccc(9, 10, 11, 12).toDict())
    print(Ccc(9, 10, 11, 12).toJson())
