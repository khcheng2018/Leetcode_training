class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        table = [['2','abc'],['3','def'],['4','ghi'],['5','jkl'],['6','mno'],['7','pqrs'],['8','tuv'],['9','wxyz']]
        length_list = []
        return_list = []
        for i in range (len(digits)):
            for j in range (len(table)):
                if (digits[i] == table[j][0]):
                    break
            return_list_temp = []
            for k in range (len(table[j][1])):
                if (return_list == []):
                    return_list_temp.append(table[j][1][k])
                else:
                    for a in range(len(return_list)):
                        string = return_list[a] + table[j][1][k]
                        return_list_temp.append(string)
            return_list = return_list_temp
        return return_list
