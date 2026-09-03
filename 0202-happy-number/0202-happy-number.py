class Solution:
    def isHappy(self, n: int) -> bool:
        if n == 1 or n == 7:
            return True
        if n < 10:
            return False
        else:
            a = 0
            while(n > 0):
                r = n % 10
                a += r**2
                n = n // 10
            return self.isHappy(a)