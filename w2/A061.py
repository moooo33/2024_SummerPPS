class Solution(object):
    def convertToTitle(self, columnNumber):
        """
        :type columnNumber: int
        :rtype: str
        """
        # 아스키 넘버를 찾아서 했는데 ord('A') 해도 됨 !
        rtn = ''
        while columnNumber > 0 :
            rtn += chr(65 + (columnNumber - 1) % 26)
            columnNumber = (columnNumber - 1) // 26 
        return rtn[::-1]