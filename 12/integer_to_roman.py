class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        string = ''
        # thosand digits
        while (num >= 1000):
            string  = string + 'M'
            num = num - 1000
        # hundreds digits
        if (num >= 900):
            string  = string + 'CM'
            num = num - 900
        elif (num >= 600):
            string  = string + 'D'
            num = num - 500
            while (num >= 100):
                string  = string + 'C'
                num = num - 100
        elif (num >= 500):
            string  = string + 'D'
            num = num - 500
        if (num >= 400):
            string  = string + 'CD'
            num = num - 400
        else:
            while (num >= 100):
                string  = string + 'C'
                num = num - 100
        # tens digits
        if (num >= 90):
            string  = string + 'XC'
            num = num - 90
        elif (num >= 60):
            string  = string + 'L'
            num = num - 50
            while (num >= 10):
                string  = string + 'X'
                num = num - 10
        elif (num >= 50):
            string  = string + 'L'
            num = num - 50

        if (num >= 40):
            string  = string + 'XL'
            num = num - 40
        else:
            while (num >= 10):
                string  = string + 'X'
                num = num - 10
        # digits
        if (num >= 9):
            string  = string + 'IX'
            num = num - 9
        elif (num >= 6):
            string  = string + 'V'
            num = num - 5
            while (num >= 1):
                string  = string + 'I'
                num = num - 1
        elif (num >= 5):
            string  = string + 'V'
            num = num - 5

        if (num >= 4):
            string  = string + 'IV'
            num = num - 4
        else:
            while (num >= 1):
                string  = string + 'I'
                num = num - 1
        return string
