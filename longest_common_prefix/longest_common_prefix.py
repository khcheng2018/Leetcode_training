class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if (len(strs) == 0):
            return ""
        length_str = []
        for i in range(len(strs)):
            length_str.append(len(strs[i]))

        min_index = length_str.index(min(length_str))
        for i in range(min(length_str)):
            for j in range(len(strs)):
                if (strs[0][i] != strs[j][j]):
                    return strs[0][0:j]
        return strs[min_index]
