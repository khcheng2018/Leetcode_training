class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        str_x = str(x)
        re_x = str_x[::-1]
        if (re_x[-1] == '-'):
            re_x = re_x[:-1]
            bool_ne = True
        else:
            bool_ne = False
        while ((re_x[0] == '0') and (len(re_x)!=1)):
            re_x = re_x[1:]
        if (int(re_x) > 2**31):
            return 0
        if (bool_ne == True):
            return (-1) * int(re_x)
        else: 
            return int(re_x)
