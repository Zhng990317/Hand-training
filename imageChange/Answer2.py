'''
最大回文数字
给你一个仅由数字(0 - 9)组成的字符串 num 。

请你找出能够使用 num 中数字形成的 最大回文 整数，并以字符串形式返回。
该整数不含 前导零 。

注意：

你 无需 使用 num 中的所有数字，但你必须使用 至少 一个数字。
数字可以重新排序。

示例 1:

输入:num = "444947137"
输出:"7449447"
解释:
从 "444947137" 中选用数字 "4449477"，可以形成回文整数 "7449447" 。
可以证明 "7449447" 是能够形成的最大回文整数。

示例 2:
输入:num = "00009"
输出："9"
解释：
可以证明 "9" 能够形成的最大回文整数。
注意返回的整数不应含前导零。

提示：

1 <= num.length <= 105
num 由数字(0 - 9)组成

'''

class Solution:
    def largestPalindromic(self, num: str) -> str:
        
        palindromicStr = ''
        numRepeat,numNotRepeat = [],[]
        for i in num:
            if i not in numNotRepeat:
                numNotRepeat.append(i) #不重复的
            else:
                numRepeat.append(i) #重复的
        if len(numNotRepeat) == len(num):
            palindromicStr = str(max(num))
        else:
            numRepeat.extend(list(set(numRepeat.copy())))
            numRepeat.sort()
            j = len(numRepeat)
            while j > 0:
                if numRepeat.count(numRepeat[j-1]) % 2 == 0:
                    pass
                else:
                    numRepeat.remove(numRepeat[j-1])
                    j -= 1
                j -= 1
            palindromic = numRepeat[::-1][0:-1:2] + numRepeat[0:-1:2]
            if palindromic.count("0") == len(palindromic):
                palindromicStr = str(max(num))
            else:
                if len(palindromic) == len(num):
                    palindromic
                else:
                    temp = []
                    for i in num:
                        if i not in palindromic:
                            temp.append(i)
                    if temp == []:
                        palindromic.insert(int(len(palindromic)/2), '0')
                    else:
                        palindromic.insert(int(len(palindromic)/2), max(temp))
                for i in palindromic:
                    palindromicStr += i
        return palindromicStr


                

num = Solution().largestPalindromic('846853515384906866969100') 
#---"988665431090134566889"
#---"846853515384906866969100"
print(num)

# class Solution:
#     def largestPalindromic(self, num: str) -> str:
#         cnt = Counter(num)
#         if cnt['0'] == len(num):  # 特判最特殊的情况：num 全是 0
#             return "0"

#         s = ""
#         for d in digits[:0:-1]:
#             s += d * (cnt[d] // 2)
#         if s:  # 如果填了数字，则可以填 0
#             s += '0' * (cnt['0'] // 2)

#         t = s[::-1]
#         for d in digits[::-1]:
#             if cnt[d] % 2:  # 还可以填一个变成奇回文串
#                 s += d
#                 break
#         return s + t  # 添加镜像部分
