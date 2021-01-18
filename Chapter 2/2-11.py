class Vector:
    def __init__(self, d):
        self._coords = [0] * d
    
    def __len__(self):
        return len(self._coords)

    def __getitem__(self, i):
        return self._coords[i]

    def __setitem__(self, i, val):
        self._coords[i] = val

    def __sub__(self, other):
        if len(self) != len(other):
            raise ValueError("dimensions must agree")
        result = Vector(len(self))
        for i in range(len(self)):
            result[i] = self[i] - other[i]
        return result

    def __neg__(self):
        result = Vector(len(self))
        for i in range(len(self)):
            result._coords[i] = -self._coords[i]
        return result
    
    def __str__(self):
        return "<" + str(self._coords)[1:-1] + ">"

    def __add__(self, other):
        if len(self) != len(other):
            raise ValueError("dimensions must agree")
        result = Vector(len(self))
        for i in range(len(self)):
            result[i] = self[i] + other[i]
        return result

    def __radd__(self, other):
        return self + other 