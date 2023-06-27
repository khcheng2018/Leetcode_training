class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        size_citations = len(citations)
        i = 0
        while (i < size_citations):
            if (citations[size_citations-i-1]>i):
                i = i + 1
            else:
                break
        return i
