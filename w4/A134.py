class Solution(object):
    def reversePrefix(self, word, ch):
        """
        :type word: str
        :type ch: str
        :rtype: str
        """
        rtn = ''
        x = 0
        for i in word:
            if i == ch:
                x = word.index(i) + 1
        
        rtn = word[:x][::-1]+word[x:]
        # print(rtn)
        return rtn