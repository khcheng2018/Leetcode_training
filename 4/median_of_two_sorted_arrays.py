class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m = len(nums1)
        n = len(nums2)
        sum_length = m + n
        new_list = []
        i = 0
        j = 0
        while ((i+j) != (m+n)):
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
        if ((sum_length % 2) == 1):
            return new_list[(sum_length/2)]
        else:
            return (float)(new_list[(sum_length/2)-1] + new_list[(sum_length/2)])/2
