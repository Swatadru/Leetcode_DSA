class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split(" ")
        l = []
        for i in s:
            element = i[::-1]
            l.append(element)
        return " ".join(l)