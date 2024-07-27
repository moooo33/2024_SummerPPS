class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.lower()
        
        letters = [letter for letter in s if letter.isalnum() == True]

        if (letters[::] == letters[::-1]):
            return True
        return False