class Solution:
    def backspaceCompare(self, S, T):
        stack1 = []
        stack2 = []
        for i in S:
            if i != "#":
                stack1.append(i)
            elif stack1:
                stack1.pop()
        for j in T:
            if j != "#":
                stack2.append(j)
            elif stack2:
                stack2.pop()
        return stack1==stack2



obj = Solution()
S = "y#fo##f"

T = "y#f#o##f"
print(obj.backspaceCompare(S, T))