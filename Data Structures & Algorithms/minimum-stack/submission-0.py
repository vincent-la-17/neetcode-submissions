class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []
    #every time you push, push the minimum between the 2 to minstack. pop if you pop. at the end, the top of minstack is the smallest.
    def push(self, val: int) -> None:
        self.stack.append(val)
        val = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
