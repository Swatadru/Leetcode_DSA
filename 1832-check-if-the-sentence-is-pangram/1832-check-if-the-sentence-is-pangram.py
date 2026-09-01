class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        s = sorted(set(sentence))
        l = list("abcdefghijklmnopqrstuvwxyz")
        if s == l:
            return True
        else:
            return False