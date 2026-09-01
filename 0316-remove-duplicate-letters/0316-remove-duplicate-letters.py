class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack = []
        for i, ele in enumerate(s):
            if ele in stack:
                continue
            if len(stack) == 0:
                stack.append(ele)
            if ele > stack[-1]:
                stack.append(ele)
            if ele < stack[-1]:
                while stack and ele < stack[-1] and stack[-1] in s[i+1:]:
                    stack.pop(-1)
                stack.append(ele)
        return "".join(stack)