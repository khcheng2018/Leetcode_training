class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        len_s = len(s)
        len_t = len(t)
        if (len_s != len_t):
            return False
        for i in range (len(string.ascii_lowercase)):
            s = s.replace(string.ascii_lowercase[i],'')
            t = t.replace(string.ascii_lowercase[i],'')
            if (len(s) != len(t)):
                return False
        return True
