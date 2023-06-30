class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        sum_length = m + n
        new_list = []
        i = 0
        j = 0
        while ((i+j) != (sum_length)):
            if (i == m):
                new_list.append(nums2[j])
                j = j + 1
            elif (j == n):
                new_list.append(nums1[i])
                i = i + 1
            elif (nums1[i]>=nums2[j]):
                new_list.append(nums2[j])
                j = j + 1
            elif (nums2[j]>nums1[i]):
                new_list.append(nums1[i])
                i = i + 1
            else:
                break
        nums1[:] = new_list
