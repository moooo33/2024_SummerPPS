class Solution(object):
    def halvesAreAlike(self, s):
        """
        :type s: str
        :rtype: bool
        """
        vowel = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        half = int(len(s)/2)
        a, b = s[:half], s[half:]
        cnt_a, cnt_b = 0, 0

        for i in range(half) : 
            if a[i] in vowel : cnt_a += 1
            if b[i] in vowel : cnt_b += 1
        
        if cnt_a == cnt_b : return True
        return False
        