class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        i = 0
        while i < len(nums):
            j = i + 1
            while j < len(nums):
                if ((nums[i]+nums[j])==target):
                    mylist = [i,j]
                    return mylist
                j = j + 1
            i = i + 1
