class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        attend_dict = {'A':0, 'L':0, 'P':0}
        print(s.count("LLL"))
        for i in s:
            attend_dict[i] = attend_dict.get(i,0)+1
        return attend_dict['A'] < 2 and s.count("LLL") == 0