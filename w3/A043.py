class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        ss, tt = [], []

        for i in range(len(s)) : 
            if s[i] == '#' : 
                if len(ss) > 0:
                    ss.pop()
                continue
            ss.append(s[i])
                
        for i in range(len(t)) : 
            if t[i] == '#' : 
                if len(tt) > 0:
                    tt.pop()
                continue
            tt.append(t[i])

        # print(ss, tt)
        return ss == tt