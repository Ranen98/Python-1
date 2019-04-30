class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        # 最小栈，压栈：每次执行完成后 把最小的压进去
        self.minStack = []

    def push(self, x: int) -> None:
        self.stack.append(x)
        if not self.minStack or x <= self.minStack[-1]:
            self.minStack.append(x)

    def pop(self) -> None:
        if self.minStack[-1] == self.stack[-1]:
            del self.minStack[-1]
        self.stack.pop()

    def top(self) -> int:
        top_element = self.stack[-1]
        return top_element

    def getMin(self) -> int:
        return self.minStack[-1]

p = MinStack()

p.push(3)
p.push(5)
p.push(2)
# p.pop()
# print(p.pop())
# print(p.top())
print(p.getMin())

