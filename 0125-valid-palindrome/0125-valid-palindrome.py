class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.replace(" ","")
        s = s.lower()
        string = ""
        for i in s:
            if i.isalnum():
                string += i
        if string == string[::-1]:
            return True
        else:
            return False