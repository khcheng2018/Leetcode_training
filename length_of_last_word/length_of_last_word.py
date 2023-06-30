class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        while (s[-1] == ' '):
            s = s[:-1]
        count = 0
        while (s != ''):
            if (s[-1] != ' '):
                s = s[:-1]
                count = count + 1
            else:
                break
        return count
