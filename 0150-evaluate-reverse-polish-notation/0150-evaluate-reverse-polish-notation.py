class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if (len(token)==1 and ord(token)<48):
                integer2 = stack.pop()
                integer1 = stack.pop()
                operator = token
                resolved_ans = self.resolves(integer1, integer2, operator)
                stack.append(resolved_ans)
            else:
                stack.append(int(token))
        return stack.pop()

        
    def resolves(self, a, b, operator):
        if operator == "+":
            return a + b
        elif operator == "-":
            return a - b
        elif operator == "*":
            return a * b
        else:
            return int(a/b)