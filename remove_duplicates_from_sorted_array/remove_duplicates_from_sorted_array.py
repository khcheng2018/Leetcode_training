class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        list_return = [nums[0]]
        num_value = nums[0]
        for i in range (len(nums)):
            if (nums[i]>num_value):
                list_return.append(nums[i])
                num_value = nums[i]
        nums[:] = list_return
