class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        size_citations = len(citations)
        i = 0
        while (i < size_citations):
            count = 0
            j = 0
            while (j < size_citations):
                if (citations[j]>i):
                    count = count + 1
                j = j + 1
            if ((count > i) and (i < size_citations)):
                i = i + 1
            else:
                return i
        return i
