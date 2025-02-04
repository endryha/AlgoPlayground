class Interval:
    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end

    def __str__(self):
        return f"{self.start}..{self.end}"

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return self.start == other.start and self.start == other
