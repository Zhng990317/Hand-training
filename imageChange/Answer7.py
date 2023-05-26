'''
剑指 Offer 60. n个骰子的点数
把n个骰子扔在地上,所有骰子朝上一面的点数之和为s。输入n,打印出s的
所有可能的值出现的概率。

你需要用一个浮点数数组返回答案，其中第 i 个元素代表这 n 个骰子所能掷出的点数集合
中第 i 小的那个的概率。

示例 1:
输入: 1
输出: [0.16667,0.16667,0.16667,0.16667,0.16667,0.16667]

示例 2:
输入: 2
输出: [0.02778,0.05556,0.08333,0.11111,0.13889,0.16667,0.13889,
0.11111,0.08333,0.05556,0.02778]
 
限制：
1 <= n <= 11
'''

class Solution:
    def dicesProbability(self, n: int) -> list[float]:
        '''n个骰子的点数'''
        # arr, result, probability = [1,2,3,4,5,6], [], []
        # arr.extend(arr*(n-1))
        # arr.sort()
        # print(arr)
        # i =  0
        # if n == 1:
        #     result = arr
        # else:
        #     while i < len(arr):
        #         j = len(arr)-1
        #         while j > i:
        #             result.append(arr[i]+arr[j])
        #             j -= 1
        #         i += 1
        #     result.sort()
        # print(result)
        # for i in list(set(result)):
        #     appears = int(result.count(i))
        #     probability.append(round(appears/int(len(result)),5))
        # print(probability)
        # print(len(result))
        #--------------------------------上面实现有问题---------------
        arr = [1,2,3,4,5,6]
        pre = [1/6]*6 #单个骰子各点出现的概率
        i = 2
        while i <= n: #从2个骰子开始计算
            result = [0]*(i*max(arr)-i*min(arr) + 1)#初始化长度列表。概率组成列表的长度=最大-最小+1
            # print(pre)
            for j in range(len(pre)):
                for k in range(6):
                    # print(result)
                    result[j+k] += pre[j]/6 #n个骰子出现概率组
            pre = result
            i += 1
        
        print([round(_,5) for _ in pre])
        return [round(_,5) for _ in pre]
    
    
# Solution().dicesProbability(1)
Solution().dicesProbability(3)
