#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
# 100. 删除排序数组中的重复数字,题目地址：https://www.lintcode.com/problem/remove-duplicates-from-sorted-array/description
# 给定一个排序数组，在原数组中删除重复出现的数字，使得每个元素只出现一次，并且返回新的数组的长度。
# 不要使用额外的数组空间，必须在原地没有额外空间的条件下完成。
# 样例:
# 样例 1:输入:[],输出: 0
# 样例 2:输入:[1,1,2],输出: 2.解释:数字只出现一次的数组为: [1,2]
'''

import unittest


class TestCases(unittest.TestCase):
    def setUp(self):
        self.solutionCase = Solution()
        
    def test_0(self):
        result = self.solutionCase.removeDuplicates([])
        expect = 0
        self.assertEqual(result, expect)
        
    def test_1(self):
        result = self.solutionCase.removeDuplicates([1,1,2])
        expect =  2
        self.assertEqual(result, expect)
        
    def test_2(self):
        result = self.solutionCase.removeDuplicates([-14,-14,-13,-13,-13,-13,-13,-13,-13,-12,-12,-12,-12,-11,-10,-9,-9,-9,-8,-7,-5,-5,-5,-5,-4,-3,-3,-2,-2,-2,-2,-1,-1,-1,-1,-1,0,1,1,1,1,2,2,2,3,3,3,4,4,4,4,5,5,5,6,6,6,6,7,8,8,8,9,9,9,10,10,10,11,11,11,12,12,12,13,14,14,14,14,15,16,16,16,18,18,18,19,19,19,19,20,20,20,21,21,21,21,21,21,22,22,22,22,22,23,23,24,25,25])
        expect = len([-14,-13,-12,-11,-10,-9,-8,-7,-5,-4,-3,-2,-1,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,18,19,20,21,22,23,24,25])
        self.assertEqual(result, expect)
        
    def test_3(self):
        result = self.solutionCase.removeDuplicates([2])
        expect = 1
        self.assertEqual(result, expect)


class Solution:
    """
    @param: nums: An ineger array
    @return: An integer
    """
    def removeDuplicates(self, nums):
        pos = i = 0
        while i < len(nums):
            if nums[pos] ^ nums[i]:
                nums[pos+1] = nums[i]
                pos +=1            
            i += 1
        pos += len(nums)>0
        nums = nums[:pos]
        return pos


if __name__ == '__main__':
    unittest.main()
