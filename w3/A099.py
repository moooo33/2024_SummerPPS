class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        brackets = {'(': ')', '{': '}', '[': ']'}
        for b in s:
            if b in brackets:
                stack.append(b)
            elif not stack:
                return False
            elif brackets[stack.pop()] != b:
                return False
        
        return not stack