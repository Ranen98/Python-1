'''
在一个二维数组中（每个一维数组的长度相同），每一行都按照从左到右递增的顺序排序，每一列
都按照从上到下递增的顺序排序。请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。
'''

class Solution():
    def Find(self, target, array):
        row = 0
        col = len(array[0])-1
        while col >= 0 and row < len(array):
            if array[row][col] == target:
                return True
            elif array[row][col] < target:
                row += 1
            else:
                col -= 1

        return False

p = Solution()
list = [[1,2,8,9],[2,4,9,12],[4,7,10,13],[6,8,11,15]]
tar = 16
print(p.Find(tar, list))