class Solution(object):
    def transpose(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        rtn = [[0] * len(matrix) for i in range(len(matrix[0]))]
        for i in range(len(matrix[0])) :
            for j in range(len(matrix)) :
                rtn[i][j] = matrix[j][i]
        return rtn
