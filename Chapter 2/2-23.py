from abc import ABCMeta, abstractmethod


class Sequence:(metaclass=ABCMeta):
    @abstractmethod
    def __len__(self):
        """Return the length of a sequence"""

    @abstractmethod
    def __getitem__(self, i):
        """Return the element at index i of the sequence"""

    def __contains__(self, val):
        for i in range(len(self)):
            if self[i] == val:
                return True
        return False

    def index(self, val):
        for i in range(len(self)):
            if self[i] == val:
                return i
        raise ValueError("value not in sequence")

    def count(self, val):
        k = 0
        for i in range(len(self)):
            if self[i] == val:
                k += 1
        return k

    def __eq__(self, other):
        if len(self) != len(other):
            raise ValueError("lengths must agree")
        for i in range(len(self)):
            if self[i] != other[i]:
                return False
        return True

    def __lt__(self, other):
        if len(self) != len(other):
            raise ValueError("lengths must agree")
        for i in range(len(self)):
            if self[i] >= other[i]:
                return False
        return True