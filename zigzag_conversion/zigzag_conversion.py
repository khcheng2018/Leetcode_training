class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        len_s = len(s)
        bool_direction = True
        rows = 0
        list_all = [''] * numRows
        string = ''
        if (numRows == 1):
            return s
        for i in range (len_s):
            list_all[rows] = list_all[rows] + s[i]
            if (bool_direction):
                if (rows < (numRows-1)):
                    rows = rows + 1
                else: 
                    rows = rows - 1
                    bool_direction = False
            else:
                if (rows != 0):
                    rows = rows - 1
                else: 
                    rows = rows + 1
                    bool_direction = True
        for j in range (numRows):
            string = string + str(list_all[j])
        return string
