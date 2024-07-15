class Solution(object):
# 범위 내에서 소수 개수(p)를 찾기
# p! * (n - p)!
    def numPrimeArrangements(self, n):
        def isPrime(num) :
            if num == 1 : return False
            for i in range(2, num) :
                if num % i == 0 : return False
            return True

        def factorial(num) :
            cnt = 1
            for i in range(1, num+1) : cnt *= i
            return cnt

        prime = 0
        for i in range(1, n+1) : 
            if isPrime(i) : prime += 1

        rtn = factorial(prime) * factorial(n - prime)
        print(prime, factorial(prime), factorial(n - prime))
        return rtn % (10**9 + 7)