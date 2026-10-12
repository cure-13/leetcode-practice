# Problem: 344.反转字符串
# Type: 双指针
# Key Insight:反转即是位置互换，python负下标自带隐藏长度
class Solution:
    def reverseString(self, s: list[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left=0
        right=len(s)-1
        while left<right:
            s[left],s[right] = s[right],s[left]
            left+=1
            right-=1    # Time: O(n)     Space: O(1) 

'''            
class Solution:
    def reverseString(self, s: List[str]) -> None:
        for i in range(len(s) // 2):
            s[1], s[-i - 1] = s[-i - 1], s[1]   # Time: O(n)     Space: O(1)
'''
#切片也可以实现反转字符串 可以直接赋值：s[:]=s[::-1] 这样时间，空间复杂度都为n（s[::-1]会临时创建新列表存放反转结果）