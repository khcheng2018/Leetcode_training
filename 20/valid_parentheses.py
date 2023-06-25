class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if ((len(s) % 2) == 1):
            return False
        i = 0
        while (s != ''):
            if ((len(s)%2 == 1) or (i == (len(s)-1))):
                return False
            elif (((s[i]=='[') and (s[i+1]==']')) or ((s[i]=='{') and (s[i+1]=='}')) or ((s[i]=='(') and (s[i+1]==')'))):
                s = s[:i] + s[i+2:]
                if (i != 0):
                    i = i - 1 
            elif (((s[i]=='[') and ((s[i+1]=='}') or (s[i+1]==')')))):
                return False
            elif (((s[i]=='(') and ((s[i+1]=='}') or (s[i+1]==']')))):
                return False
            elif (((s[i]=='{') and ((s[i+1]==']') or (s[i+1]==')')))):
                return False
            else:
                i = i + 1
        return True
