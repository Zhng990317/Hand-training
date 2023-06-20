'''
剑指 Offer 61. 扑克牌中的顺子
从若干副扑克牌中随机抽 5 张牌,判断是不是一个顺子,即这5张牌是不是连续的。2~10为数字本身,
A为1,J为11,Q为12,K为13,而大、小王为 0 ,可以看成任意数字。A 不能视为 14。

示例 1:
输入: [1,2,3,4,5]
输出: True
 
示例 2:
输入: [0,0,1,2,5]
输出: True
 
限制：
数组长度为 5 
数组的数取值为 [0, 13] .
'''
class Solution:
    def isStraight(self, nums: list[int]) -> bool:
        '''扑克牌中的顺子'''
        p = [i for i in nums if i] #遍历nums取出非0数字
        if len(set(p)) != len(p):#判断去重后长度是否与原长度相等
            return False
        return max(p)-min(p) < 5 #判断最大值减最小值＜5


                

        
print(Solution().isStraight([0,1,3,2,5]))
print(Solution().isStraight([0,1,2,2,5]))
print(Solution().isStraight([1,2,3,4,5]))
print(Solution().isStraight([0,0,1,2,5]))