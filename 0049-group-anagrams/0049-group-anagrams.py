class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for eachWord in strs:
            sorted_words = ''.join(sorted(eachWord))
            if sorted_words in anagrams:
                anagrams[sorted_words].append(eachWord)
            else:
                anagrams[sorted_words] = [eachWord]
        return list(anagrams.values())