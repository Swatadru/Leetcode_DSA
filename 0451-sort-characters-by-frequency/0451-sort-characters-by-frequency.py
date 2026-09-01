class Solution:
    def frequencySort(self, s: str) -> str:
        elements = []
        frequency = []
        for i in s:
            count = s.count(i)
            frequency.append(count)
            elements.append(i)
        pairs = zip(frequency, elements)
        sorted_pairs = sorted(pairs, reverse=True)
        return "".join(char for freq, char in sorted_pairs)