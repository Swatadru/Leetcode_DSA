class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
        return return_all_words(digits)


keys = {"1":"","2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}

def return_all_words(inputs):
    if inputs=="":
        return [""]
    
    ans = []
    smallestInput = inputs[1:]
    smallestInputWord = return_all_words(smallestInput)

    keyLetter = keys[inputs[0]]

    for char in keyLetter:
        for word in smallestInputWord:
            ans.append(char + word)
    return ans