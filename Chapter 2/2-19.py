class Progression:
    def __init__(self, start=0):
        self._current = start

    def __next__(self):
        if self._current is None:
            raise StopIteration()
        result = self._current
        self._advance()
        return result

    def __iter__(self):
        return self

    def print_progression(self, n):
        print(" ".join(str(next(self)) for i in range(n)))

    def _advance(self):
        self._current += 1


class FibonacciProgression(Progression):
    def __init__(self, first=0, second=1):
        super().__init__(first)
        self._prev = second - first

    def _advance(self):
        self._prev, self._current = self._current, self._prev + self._current 


class ArithmeticProgression(Progression):
    def __init__(self, increment=1, start=0):
        super().__init__(start)
        self._increment = increment

    def _advance(self):
        self._current += self._increment


if __name__ == "__main__":
    print(int((2 ** 63) / 128))