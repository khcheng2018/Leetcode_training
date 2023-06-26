class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        i = 0
        while (True):
            if ((i*i)<=x):
                i = i + 1
            else:
                return (i - 1)
