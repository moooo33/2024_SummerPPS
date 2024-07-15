class MinStack(object):

    def __init__(self):
        self.arr = []
        self.min_s = []
        

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.arr.append(val)
        if len(self.min_s) == 0 or val <= self.min_s[-1] : self.min_s.append(val)


    def pop(self):
        """
        :rtype: None
        """
        popped = self.arr.pop()
        if self.min_s and popped == self.min_s[-1] : # 스택이 비어있지 않은 경우
            self.min_s.pop()


    def top(self):
        """
        :rtype: int
        """
        if self.arr : return self.arr[-1]
        return -1 # 예외 처리 유의하기 !


    def getMin(self):
        """
        :rtype: int
        """
        if self.min_s : return self.min_s[-1]
        return -1