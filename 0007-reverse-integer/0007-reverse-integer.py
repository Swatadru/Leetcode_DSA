class Solution:
    def reverse(self, x: int) -> int:
        return revNum(x)

def revNum(n):
    if n > 0:
        rev = str(n)[::-1]
        if rev[0] == "0":
            result = int(rev[1:])
        else:
            result = int(rev)
    elif n == 0:
        result = n
    else:
        n = str(n)
        original_length = len(n)
        rev = n[original_length:: -1]
        result = int("-" + rev[:-1])
        
    if (-2)**31 <= result <= (2**31) - 1:
        return result 
    else:
        return 0