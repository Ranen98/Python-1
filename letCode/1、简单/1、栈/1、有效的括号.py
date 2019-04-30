class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        mapping = {")": "(", "}": "{", "]": "["}

        for char in s:
            if char not in mapping:
                stack.append(char)
            else:
                top_element = stack.pop() if stack else "#"
                if mapping[char] != top_element:
                    return False
        return not stack


p = Solution()
str1 = "()"
print(p.isValid(str1))
