class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        person = []
        index = 0
        for i in range(1, n + 1):
            person.append(i)
        while len(person) > 1:
            index = (index + k - 1) % len(person)
            person.pop(index)
        return person[0]