"""
给你两个按 非递减顺序 排列的整数数组 nums1 和 nums2,另有两个整数 m 和 n ,分别表示 nums1 和 nums2 中的元素数目。
请你 合并 nums2 到 nums1 中，使合并后的数组同样按 非递减顺序 排列。
注意：最终，合并后数组不应由函数返回，而是存储在数组 nums1 中。为了应对这种情况,nums1 的初始长度为 m + n,其中前 m 个元素
表示应合并的元素,后 n 个元素为 0 ,应忽略。nums2 的长度为 n 。

示例 1:
输入:nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
输出:[1,2,2,3,5,6]
解释:需要合并 [1,2,3] 和 [2,5,6] 。
合并结果是 [1,2,2,3,5,6] ，其中斜体加粗标注的为 nums1 中的元素。

示例 2:
输入:nums1 = [1], m = 1, nums2 = [], n = 0
输出:[1]
解释:需要合并 [1] 和 [] 。
合并结果是 [1] 。

示例 3:
输入:nums1 = [], m = 0, nums2 = [1], n = 1
输出:[1]
解释:需要合并的数组是 [] 和 [1] 。
合并结果是 [1] 。
注意，因为 m = 0 ,所以 nums1 中没有元素。nums1 中仅存的 0 仅仅是为了确保合并结果可以顺利存放到 nums1 中。

提示:
nums1.length == m + n
nums2.length == n
0 <= m, n <= 200
1 <= m + n <= 200
-109 <= nums1[i], nums2[j] <= 109
"""
def lists_merge(nums1:list, nums2:list,m:int,n:int):
    # nums1[m:] = nums2
    # nums1.sort()
    temp = 0
    if n == 0:
        nums1
    else:
        nums1.extend(nums2)
        nums1.sort()
        for i in range(len(nums1)):   
            if nums1[i] == 0:
                temp = i
                break
        del nums1[temp:temp+n]
    print(nums1)

lists_merge([1], [0], 1, 0)
lists_merge([0], [1], 0, 1)
lists_merge([1, 2, 3, 0, 0, 0], [2, 5, 6], 3, 3)
lists_merge([-1,0,0,3,3,3,0,0,0],[1,2,2],9,3)
