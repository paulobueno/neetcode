# URL https://neetcode.io/problems/minimum-stack
# Time Complexity: O(1)
# Space Complexity: O(N)

class MinStack:

    def __init__(self):
        self.stack = []
        self.min = None

    def push(self, val: int) -> None:
        if self.min is None:
            self.min = val
        self.stack.append(val - self.min)
        if val < self.min:
            self.min = val

    def pop(self) -> None:
        popped = self.stack.pop()
        if popped < 0:
            self.min += abs(popped)
        if not len(self.stack):
            self.min = None

    def top(self) -> int:
        return self.stack[-1] + self.min if self.stack[-1] >= 0 else self.min

    def getMin(self) -> int:
        return self.min
