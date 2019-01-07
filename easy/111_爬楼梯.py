#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
# 111. 爬楼梯,题目地址：https://www.lintcode.com/problem/climbing-stairs/description
# 假设你正在爬楼梯，需要n步你才能到达顶部。但每次你只能爬一步或者两步，你能有多少种不同的方法爬到楼顶部？
# 样例:比如n=3，1+1+1=1+2=2+1=3，共有3种不同的方法，返回 3
'''

import unittest


class TestCases(unittest.TestCase):
    def setUp(self):
        self.solutionCase = Solution()
        
    def test_0(self):
        result = self.solutionCase.climbStairs(0)
        expect = 0
        self.assertEqual(result, expect)
        
    def test_1(self):
        result = self.solutionCase.climbStairs(1)
        expect =  1
        self.assertEqual(result, expect)
        
    def test_2(self):
        result = self.solutionCase.climbStairs(2)
        expect = 2
        self.assertEqual(result, expect)
        
    def test_3(self):
        result = self.solutionCase.climbStairs(39)
        expect = 102334155
        self.assertEqual(result, expect)
    

'''
# 解法一，递归，超时：
class Solution:
    """
    @param n: An integer
    @return: An integer
    """
    def climbStairs(self, n):
        # return 1/(5**0.5)*(((1+(5**0.5))/2)**(n)-((1-(5**0.5))/2)**(n))
        if n == 1:
            result = 1
        elif n == 2:
            result = 2
        elif n == 0:
            result = 0
        else:
            result = self.climbStairs(n-1) + self.climbStairs(n-2)
        return result
'''


# 解法二，递推：
class Solution:
    """
    @param n: An integer
    @return: An integer
    """
    def climbStairs(self, n):
        a, b = 0, 1   
        if n == 0:
            pass
        else:
            for i in range(n+1):
                a, b = b, a+b
        return a
        
        
if __name__ == '__main__':
    unittest.main()
