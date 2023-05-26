# region Solution
'''
205. 同构字符串
给定两个字符串 s 和 t ，判断它们是否是同构的。

如果 s 中的字符可以按某种映射关系替换得到 t ，那么这两个字符串是同构的。

每个出现的字符都应当映射到另一个字符，同时不改变字符的顺序。不同字符不能映射到
同一个字符上，相同字符只能映射到同一个字符上，字符可以映射到自己本身。

示例 1:
输入:s = "egg", t = "add"
输出:true

示例 2:
输入:s = "foo", t = "bar"
输出:false

示例 3:
输入:s = "paper", t = "title"
输出:true
 

提示:
1 <= s.length <= 5 * 104
t.length == s.length
s 和 t 由任意有效的 ASCII 字符组成
'''
'''
解题过程：
1.获取索引,使用index()
2.将索引添加到列表,再对比列表
'''


# endregion
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        '''同构字符串'''
        if len(s) != len(t):
            return False
        if self.indexString(s) == self.indexString(t):
            return True
        else:
            return False

    def indexString(self, v:str):
        indexString = []
        for i in range(len(v)):
            indexString.append(v.index(v[i]))
        print(indexString)
        return indexString

        

# print(Solution().isIsomorphic(s='egg',t='add'))#011--011
# print(Solution().isIsomorphic(s='foo',t='bar'))#011--012
# print(Solution().isIsomorphic(s='paper',t='title'))#01034--01034
print(Solution().isIsomorphic(s='abcdefghijklmnopqrstuvwxyzva',t='abcdefghijklmnopqrstuvwxyzck'))
# "abcdefghijklmnopqrstuvwxyzva"
# --012345678910111213141516171819202122232425210
# "abcdefghijklmnopqrstuvwxyzck"
# --012345678910111213141516171819202122232425210