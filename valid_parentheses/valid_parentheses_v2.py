class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s_before = s
        s_after = s
        while (s_after != ''):
            s_after = s_before.replace('()','')
            s_after = s_after.replace('[]','')
            s_after = s_after.replace('{}','')
            if (s_after == s_before):
                return False
            s_before = s_after
        return True
