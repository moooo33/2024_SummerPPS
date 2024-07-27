class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        rtn = []
        for i in range(left, right+1):
            isDivided = False
            for j in str(i) : 
                if j == '0' : 
                    isDivided = False
                    break
                if i % int(j) == 0 : isDivided = True
                else : 
                    isDivided = False
                    break
                    
            if isDivided == True : rtn.append(i)
        return rtn