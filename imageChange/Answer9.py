'''
面试题 05.01. 插入
给定两个整型数字 N 与 M,以及表示比特位置的 i 与 j(i <= j,且从 0 位开始计算)。

编写一种方法，使 M 对应的二进制数字插入 N 对应的二进制数字的第 i ~ j 位区域，
不足之处用 0 补齐。具体插入过程如图所示。

题目保证从 i 位到 j 位足以容纳 M,例如： M = 10011,则 i~j 区域至少可容纳 5 位。

示例1:
 输入:N = 1024(10000000000), M = 19(10011), i = 2, j = 6
 输出:N = 1100(10001001100)
示例2:
 输入: N = 0, M = 31(11111), i = 0, j = 4
 输出:N = 31(11111)
'''
#关键词：位运算
class Solution:
    def insertBits(self, N: int, M: int, i: int, j: int) -> int:

        binaryN = bin(N).removeprefix('0b')
        binaryM = bin(M).removeprefix('0b')
        binaryNList = [_ for _ in binaryN][::-1] if N != 0 else []
        if len(binaryM) != (j - i + 1):
            binaryNList[i : j + 1] = binaryM[::-1] + "0"*((j - i + 1) - len(binaryM))
        else:
            binaryNList[i : j + 1] = binaryM[::-1]
        strN = ''
        for i in binaryNList[::-1]:
            strN += str(i)
        N = int(strN,2)
        return N

Solution().insertBits(1024,19,2,6)#1100
Solution().insertBits(0,31,0,4)#31
Solution().insertBits(645256491,151292,0,22)#637685500