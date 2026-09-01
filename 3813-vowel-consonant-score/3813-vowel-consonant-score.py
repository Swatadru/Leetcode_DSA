class Solution:
    def vowelConsonantScore(self, s: str) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        v = 0
        c = 0

        for ch in s:
            if ch.isalpha():
                if ch in vowels:
                    v += 1
                else:
                    c += 1

        if c == 0:
            return 0
        return v // c