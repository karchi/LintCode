#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
# 37. 反转一个3位整数,题目地址：https://www.lintcode.com/problem/reverse-3-digit-integer/description
# 反转一个只有3位数的整数。
'''

import unittest


class TestCases(unittest.TestCase):
    def setUp(self):
        self.solutionCase = Solution()
        
    def test_123(self):
        result = self.solutionCase.reverseInteger(123)
        expect = 321
        self.assertEqual(result, expect)
        
    def test_900(self):
        result = self.solutionCase.reverseInteger(900)
        expect = 9
        self.assertEqual(result, expect)
        
    def test_555(self):
        result = self.solutionCase.reverseInteger(555)
        expect = 555
        self.assertEqual(result, expect)
    

# 解法1：
class Solution:
    """
    @param number: A 3-digit number.
    @return: Reversed number.
    """
    def reverseInteger(self, number):
        return int(str(number)[::-1])


'''
# 解法2：
class Solution:
    """
    @param number: A 3-digit number.
    @return: Reversed number.
    """
    def reverseInteger(self, number):
        return number % 10 * 100 + number // 10 % 10 * 10 + number // 100
'''


if __name__ == '__main__':
    unittest.main()
