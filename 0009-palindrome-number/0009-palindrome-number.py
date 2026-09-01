class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        reverse_number = 0
        original_number = x
        while x>0:
            digits = x % 10
            reverse_number = reverse_number*10 + digits
            x //= 10
        return original_number == reverse_number