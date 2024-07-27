# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        l, h = 0, n

        while l <= h:
            mid = (l + h)//2
            print(mid)
            if guess(mid) == -1:
                h = mid - 1
            elif guess(mid) == 1:
                l = mid + 1
            elif guess(mid) == 0:
                return mid