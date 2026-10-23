class MinStack:
    def __init__(self):
        self.minNum = None
        self.stack = []

    def push(self, val: int) -> None:
        if self.stack:
            self.minNum = min(self.minNum, val)
        else:
            self.minNum = val
        self.stack.append((val, self.minNum))

    def pop(self) -> None:
        self.stack.pop()

        if self.stack:
            self.minNum = self.getMin()
        else:
            self.minNum = None

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]
