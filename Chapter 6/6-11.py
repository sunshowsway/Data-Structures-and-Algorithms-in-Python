from collections import deque


class ArrayQueue:
    
    def __init__(self):
        self._data = deque()

    def __len__(self):
        return len(self._data)
    
    def is_empty(self):
        return len(self._data) == 0

    def first(self):
        if len(self._data) == 0:
            raise Exception("Queue is empty")
        return self._data[0]

    def dequeue(self):
        if len(self._data) == 0:
            raise Exception("Queue is empty")
        return self._data.popleft()

    def enqueue(self, e):
        self._data.append(e)