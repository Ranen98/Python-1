class Solution:
    def nextGreaterElement(self, nums1, nums2):
        dic, stack = {}, []
        for number in nums2:
            while stack and stack[-1] < number:
                dic[stack.pop()] = number
            stack.append(number)
        return [dic.get(i, -1) for i in nums1]
obj = Solution()
nums1 = [1, 3, 5, 2, 4]
nums2 = [6, 5, 4, 3, 2, 1, 7]

print(obj.nextGreaterElement(nums1, nums2))

