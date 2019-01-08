#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
# 539. 移动零,题目地址：https://www.lintcode.com/problem/move-zeroes/description
# 给一个数组 nums 写一个函数将 0 移动到数组的最后面，非零元素保持原数组的顺序
# 1.必须在原数组上操作
# 2.最小化操作数
# 样例:给出 nums = [0, 1, 0, 3, 12], 调用函数之后, nums = [1, 3, 12, 0, 0].
'''

import unittest


class TestCases(unittest.TestCase):
    def setUp(self):
        self.solutionCase = Solution()
        
    def test_0(self):
        result = self.solutionCase.moveZeroes([0, 1, 0, 3, 12])
        expect = [1, 3, 12, 0, 0]
        self.assertEqual(result, expect)
        
    def test_1(self):
        result = self.solutionCase.moveZeroes([-1,2,-3,4,0,1,0,-2,0,0,1])
        expect =  [-1,2,-3,4,1,-2,1,0,0,0,0]
        self.assertEqual(result, expect)

    
'''
# 解法一：
class Solution:
    """
    @param nums: an integer array
    @return: nothing
    """
    def moveZeroes(self, nums):
        count = 0
        for i in nums[:]:
            if i == 0:
                nums.remove(i)
                count += 1
        nums.extend(count*[0])
        return nums
'''

# 解法二，双指针：
class Solution:
    """
    @param nums: an integer array
    @return: nothing
    """
    def moveZeroes(self, nums):
        j = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                j = max(i, j)
                while j < len(nums) and nums[j] == 0:
                    j += 1
                if j < len(nums):
                    nums[i], nums[j] = nums[j], nums[i]
                else:
                    break
        return nums
       
       
if __name__ == '__main__':
    unittest.main()
