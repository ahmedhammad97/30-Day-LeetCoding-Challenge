class MinStack:
    def __init__(self):
        self.stack = list()
        
    def push(self, x: int) -> None:
        self.stack.append(x, min(x, self.getMin()))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0] if self.stack else None

    def getMin(self) -> int:
        return self.stack[-1][1] if self.stack else 2**31


# A simple approach is to save the minimum for every state of the stack,
# thus by modifying it by any means, the stack still preserves its minimum.

# Instead of storing the minimum in a separate stack, I added it to the main
# stack's value, wrapping both of them in a tuple, thus coupling them together,
# and avoiding any mapping issues.

# A constant space approach exists.