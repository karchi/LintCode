#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
# 1112. 寻找数据错误,题目地址：https://www.lintcode.com/problem/set-mismatch/description
# 集合S本是包含数字1到n。但很不幸，由于数据错误，集合中的一个数重复为了另一个数。给定数组nums，表示发生错误后的数组，以数组的形式返回重复的数值和缺失的数值。
# 1.数组的大小范围为[2, 10000]。
# 2.数组元素是无序的。
# 样例:输入: nums = [1,2,2,4]输出: [2,3]
'''

import unittest


class TestCases(unittest.TestCase):
    def setUp(self):
        self.solutionCase = Solution()
        
    def test_0(self):
        result = self.solutionCase.findErrorNums([1,2,2,4])
        expect = [2,3]
        self.assertEqual(result, expect)
        
    def test_1(self):
        result = self.solutionCase.findErrorNums([1,1])
        expect =  [1,2]
        self.assertEqual(result, expect)
        
    def test_2(self):
        result = self.solutionCase.findErrorNums([3,2,3,4,6,5])
        expect = [3,1]
        self.assertEqual(result, expect)
        
'''
# 解法一,超时：
class Solution:
    """
    @param nums: an array
    @return: the number occurs twice and the number that is missing
    """
    def findErrorNums(self, nums):
        all = list(range(1, len(nums)+1))
        for i in all:
            if i in nums:
                nums.remove(i)
            else:
                nums.append(i)
        return nums
'''

# 解法二：
class Solution:
    """
    @param nums: an array
    @return: the number occurs twice and the number that is missing
    """
    def findErrorNums(self, nums):
        all = [0]*len(nums)
        for i in nums:
            if all[i-1]:
                res = i
            else:
                all[i-1] = i
        return [res,all.index(0)+1]

        
if __name__ == '__main__':
    unittest.main()
