class Solution(object):
    def firstMissingPositive(self, nums):
        s=set(x for x in nums if x>0)
        for i in range(1,len(nums)+2):
            if i not in s:
                return i
