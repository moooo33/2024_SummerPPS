class Solution(object):
    def maxNumberOfBalloons(self, text):
        """
        :type text: str
        :rtype: int
        """
        ditgit = {'b':0, 'a':0, 'n':0, 'l':0, 'o':0}
        for i in text:
            if i in ditgit.keys():
                ditgit[i] += 1
        count = min(ditgit['b'], ditgit['a'], ditgit['n'], ditgit['l']//2, ditgit['o']//2) # min은 여러개도 파라미터 가넝한..!
        return count