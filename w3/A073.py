class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        rtn = []
        for num in range(1, n + 1):
            if num % 3 == 0 and num % 5 == 0:
                rtn.append("FizzBuzz")
            elif num % 3 == 0:
                rtn.append("Fizz")
            elif num % 5 == 0:
                rtn.append("Buzz")
            else:
                rtn.append(str(num))

        return rtn