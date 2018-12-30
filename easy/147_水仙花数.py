#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
# 147. 水仙花数,题目地址：https://www.lintcode.com/problem/narcissistic-number/
# 水仙花数的定义是，这个数等于他每一位上数的幂次之和
# 比如一个3位的十进制整数153就是一个水仙花数。因为 153 = 13 + 53 + 33。而一个4位的十进制数1634也是一个水仙花数，因为 1634 = 14 + 64 + 34 + 44。
# 给出n，找到所有的n位十进制水仙花数。
# 你可以认为n小于8
# 样例:比如 n = 1, 所有水仙花数为：[0,1,2,3,4,5,6,7,8,9]。而对于 n = 2, 则没有2位的水仙花数，返回 []。
'''

import unittest

class TestCases(unittest.TestCase):
    def setUp(self):
        self.solutionCase = Solution()
        
    def test_0(self):
        result = self.solutionCase.getNarcissisticNumbers(1)
        expect = [0,1,2,3,4,5,6,7,8,9]
        self.assertEqual(result, expect)
        
    def test_1(self):
        result = self.solutionCase.getNarcissisticNumbers(2)
        expect = []
        self.assertEqual(result, expect)
        
    def test_2(self):
        result = self.solutionCase.getNarcissisticNumbers(3)
        expect = [153,370,371,407]
        self.assertEqual(result, expect)
    

class Solution:
    """
    @param n: The number of digits
    @return: All narcissistic numbers with n digits
    """
    def getNarcissisticNumbers(self, n):
        result = []
        if n == 1:
            start = 0
        else:
            start = 10 ** (n-1)
        for i in range(start, 10 ** n):
            temp = i
            sum = 0
            while temp>0:
                sum+=((temp%10)**n)
                if sum > i:
                    break
                temp = temp//10
            if sum == i:
                result.append(i)
        return result


if __name__ == '__main__':
    unittest.main()

