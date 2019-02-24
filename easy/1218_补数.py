#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
# 1218. 补数,题目地址：https://www.lintcode.com/problem/number-complement/description
# 给定一个正整数，输出它的补数。补数是将原先数字的二进制表示按位取反，再换回十进制后得到的新数。
# 给定的整数保证在32位有符号整数的范围内。
# 假设一个正整数的二进制表示不包含前导零。
# 样例:
# 样例1：输入：5,输出：2,说明：5的二进制表示为101（不包含前导零），它的补数为010，因此你需要输出2。
# 样例2：输入：1,输出：0,说明：1的二进制表示为1（不包含前导零），它的补数为0，因此你需要输出0。
'''

import unittest


class TestCases(unittest.TestCase):
    def setUp(self):
        self.solutionCase = Solution()
        
    def test_0(self):
        result = self.solutionCase.findComplement(5)
        expect = 2
        self.assertEqual(result, expect)
        
    def test_1(self):
        result = self.solutionCase.findComplement(1)
        expect =  0
        self.assertEqual(result, expect)
        
        
class Solution:
    """
    @param num: an integer
    @return: the complement number
    """
    def findComplement(self, num):
        return int("".join([str(1^int(s)) for s in bin(num)[2:]]),2)
        

'''
# 解法2：
class Solution:
    """
    @param num: an integer
    @return: the complement number
    """
    def findComplement(self, num):
        flipper = 1 
        while flipper <= num:
            num ^= flipper
            flipper <<= 1
        return num
'''

if __name__ == '__main__':
    unittest.main()
    
