#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
# 479. 数组第二大数,题目地址：https://www.lintcode.com/problem/second-max-of-array/description
# 在数组中找到第二大的数
'''


import unittest


class TestCases(unittest.TestCase):
    def setUp(self):
        self.solutionCase = Solution()
        
    def test_2(self):
        result = self.solutionCase.secondMax([1, 2])
        expect = 1
        self.assertEqual(result, expect)

    def test_4(self):
        result = self.solutionCase.secondMax([1, 3, 2, 4])
        expect = 3
        self.assertEqual(result, expect)
        
    def test_same(self):
        result = self.solutionCase.secondMax([1, 1, 2, 2])
        expect = 2
        self.assertEqual(result, expect)
        

'''
# 解法1：
class Solution:
    """
    @param nums: An integer array
    @return: The second max number in the array.
    """
    def secondMax(self, nums):
        nums.sort()
        return nums[-2]
'''


# 解法2：
class Solution:
    """
    @param nums: An integer array
    @return: The second max number in the array.
    """
    def secondMax(self, nums):
        max = nums[0]
        if nums[1] < max:
            second = nums[1]
        else:
            second = nums[0]
            max = nums[1]
        for i in range(2, len(nums)):
            if nums[i] <= second:
                continue
            elif nums[i] >= max:
                second = max
                max = nums[i]           
            else:
                second = nums[i]           
        return second
        
        
if __name__ == '__main__':
    unittest.main()

