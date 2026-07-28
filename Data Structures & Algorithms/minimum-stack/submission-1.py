class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        return self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        s = []
        min_ele = float("inf")

        while self.stack:
            curr = self.stack.pop()
            s.append(curr)
            if curr < min_ele:
                min_ele = curr
        
        while s:
            self.stack.append(s.pop())
        return min_ele

