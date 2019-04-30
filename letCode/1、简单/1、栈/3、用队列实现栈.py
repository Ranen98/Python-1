class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q = []
    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.q.append(x)
    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        return self.q.pop()
    def top(self) -> int:
        """
        Get the top element.
        """
        return self.q[-1]
    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return False if self.q else True

# Your MyStack object will be instantiated and called as such:
obj = MyStack()
obj.push(1)
obj.push(2)
param_2 = obj.pop()
param_3 = obj.top()
param_4 = obj.empty()
print(param_2, param_3, param_4)