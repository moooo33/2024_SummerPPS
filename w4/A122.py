class Solution(object):
    def rotateString(self, s, goal):
        """
        :type s: str
        :type goal: str
        :rtype: bool
        """
        rt = ""       
        for i in range(len(s)):
            rt = s[i:] + s[:i]
            if rt == goal:
                return True
        return False