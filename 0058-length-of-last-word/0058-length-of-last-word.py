class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        x = s.split(" ")
        for i in x[::-1]:
            if i == "":
                x.remove(i)
        return len(x[-1])