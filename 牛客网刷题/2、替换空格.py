'''
请实现一个函数，将一个字符串中的每个空格替换成“%20”。例如，当字符串为We Are Happy.则经过替换之后的字符串为We%20Are%20Happy。
'''
import re
class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        res = re.sub(r" ", "%20", s, flags=re.I)
        return res

p = Solution()
s = "hello  my name is ranen"
print(p.replaceSpace(s))