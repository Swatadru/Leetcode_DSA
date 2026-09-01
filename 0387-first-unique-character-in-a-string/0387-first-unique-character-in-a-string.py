class Solution:
    def firstUniqChar(self, s: str) -> int:
        index = 0
        while index <= len(s):
            count = s.count(s[index])
            if count>1:
                index += 1
            if count == 1:
                return index
            if count>1 and index==len(s):
                return -1