class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        total = 0
        for i in str(num) : total += int(i)
        if total > 9 : return self.addDigits(total)
        else : return total
        