#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
# 488. 快乐数,https://www.lintcode.com/problem/happy-number/description
# 写一个算法来判断一个数是不是"快乐数"。
#  一个数是不是快乐是这么定义的：对于一个正整数，每一次将该数替换为他每个位置上的数字的平方和，然后重复这个过程直到这个数变为1，或是无限循环但始终变不到1。如果可以变为1，那么这个数就是快乐数。
'''

import unittest

class TestCases(unittest.TestCase):
    def setUp(self):
        self.solutionCase = Solution()
        
    def test_0(self):
        result = self.solutionCase.isHappy(19)
        expect = True
        self.assertEqual(result, expect)
        
    def test_1(self):
        result = self.solutionCase.isHappy(1)
        expect = True
        self.assertEqual(result, expect)
        
    def test_2(self):
        result = self.solutionCase.isHappy(2)
        expect = False
        self.assertEqual(result, expect)

    
class Solution:
    """
    @param n: An integer
    @return: true if this is a happy number or false
    """
    def isHappy(self, n):
        res = True
        while n != 1:
            n = str(n)
            sum_n = 0
            for i in range(len(n)):
                sum_n += int(n[i]) ** 2
            if sum_n == 4:
                res = False
                break
            n = sum_n
        return res


if __name__ == '__main__':
    unittest.main()

