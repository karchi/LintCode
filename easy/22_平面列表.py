#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
# 22. 平面列表,题目地址：https://www.lintcode.com/problem/flatten-list/description
# 给定一个列表，该列表中的每个要素要么是个列表，要么是整数。将其变成一个只包含整数的简单列表。
# 样例:给定 [1,2,[1,2]]，返回 [1,2,1,2]。给定 [4,[3,[2,[1]]]]，返回 [4,3,2,1]。
# 挑战:请用非递归方法尝试解答这道题。
'''

import unittest


class TestCases(unittest.TestCase):
    def setUp(self):
        self.solutionCase = Solution()
        
    def test_0(self):
        result = self.solutionCase.flatten([1,2,[1,2]])
        expect = [1,2,1,2]
        self.assertEqual(result, expect)
        
    def test_1(self):
        result = self.solutionCase.flatten([4,[3,[2,[1]]]])
        expect =  [4,3,2,1]
        self.assertEqual(result, expect)
        
    def test_2(self):
        result = self.solutionCase.flatten([[1,1],2,[1,1]])
        expect = [1,1,2,1,1]
        self.assertEqual(result, expect)
        
    def test_3(self):
        result = self.solutionCase.flatten(10)
        expect = [10]
        self.assertEqual(result, expect)
    

# 解法一：
class Solution(object):
    # @param nestedList a list, each element in the list 
    # can be a list or integer, for example [1,2,[1,2]]
    # @return a list of integer
    def flatten(self, nestedList):
        result = []
        if isinstance(nestedList, int):
            result.append(nestedList)
        else:
            while nestedList:
                if isinstance(nestedList[0], int):
                    result.append(nestedList.pop(0))
                else:
                    nestedList = nestedList[0] + nestedList[1:]
        return result


'''
# 解法二，递归：
class Solution(object):
    # @param nestedList a list, each element in the list 
    # can be a list or integer, for example [1,2,[1,2]]
    # @return a list of integer
    def flatten(self, nestedList):
        if isinstance(nestedList,int):
            return [nestedList]
        else:
            result = []
            for item in nestedList:
                result += self.flatten(item)
            return result
'''
        
        
if __name__ == '__main__':
    unittest.main()

