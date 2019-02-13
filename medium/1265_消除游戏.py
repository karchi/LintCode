#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
# 1265. 消除游戏,题目地址：https://www.lintcode.com/problem/elimination-game/description
# 有一个从1到n的排序整数列表。从左到右，然后删除第一个数字和每隔一个数字删一个，直到到达列表末尾。再次重复上一步，但这次从右到左，从剩余的数字中删除最右边的数字和每隔一个数字删一个。我们继续重复这些步骤，从左到右，从右到左交替，直到剩下一个数字。找到长度为 n 的列表剩下的最后一个数字
# 样例:
# 输入:n = 9,
# 1 2 3 4 5 6 7 8 9
# 2 4 6 8
# 2 6
# 6
# 输出:
# 6
'''

import unittest


class TestCases(unittest.TestCase):
    def setUp(self):
        self.solutionCase = Solution()
        
    def test_0(self):
        result = self.solutionCase.lastRemaining(8)
        expect = 6
        self.assertEqual(result, expect)
        
    def test_1(self):
        result = self.solutionCase.lastRemaining(9)
        expect =  6
        self.assertEqual(result, expect)
        
    def test_2(self):
        result = self.solutionCase.lastRemaining(1)
        expect = 1
        self.assertEqual(result, expect)
        
    def test_3(self):
        result = self.solutionCase.lastRemaining(2)
        expect = 2
        self.assertEqual(result, expect)
        
        
class Solution:
    """
    @param n: a integer
    @return: return a integer
    """
    def lastRemaining(self, n):
        head = 1; interval = 1; remaining = n
        isLeft = True
        while remaining > 1:
            if isLeft or remaining % 2 == 1:
                head += interval
            remaining //= 2
            interval *= 2
            isLeft = not isLeft
        return head


if __name__ == '__main__':
    unittest.main()
