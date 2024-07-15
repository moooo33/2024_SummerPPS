import math

class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        sqrt = math.sqrt(num)
        return (int(sqrt) == float(sqrt))
        