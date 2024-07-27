class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        s_list = list(s)
        
        for letter in t:
            if letter in s_list:
                s_list.remove(letter)
            else:
                return letter