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
            count_s = 0
            count_t = 0
            for j in range (len(s)):
                if (s[j]==string.ascii_lowercase[i]):
                    count_s = count_s + 1
            for k in range (len(t)):
                if (t[k]==string.ascii_lowercase[i]):
                    count_t = count_t + 1
            if (count_s != count_t):
                return False
            s = s.replace(string.ascii_lowercase[i],'')
            t = t.replace(string.ascii_lowercase[i],'')
        return True
