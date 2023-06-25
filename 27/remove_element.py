class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        count = 0
        return_array = []
        i = 0
        for i in range (len(nums)):
            if (nums[i] != val):
                count = count + 1
                return_array.append(nums[i])
        nums[:] = return_array
        return count
