class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()
        if not s:
            return 0

        new = ""

        if s[0].isdigit():
            for i in str(s):
                if i.isdigit():
                    if new == "":
                        new = new.join(i)
                    else:
                        new += i
                else:
                    break
            result = int(new)

        elif s[0] == "-":
            for i in str(s[1:]):
                if i.isdigit():
                    if new == "":
                        new = new.join(i)
                    else:
                        new += i
                else:
                    break
            if new == "":
                return 0
            result = int(new) * -1

        elif s[0] == "+":
            for i in str(s[1:]):
                if i.isdigit():
                    if new == "":
                        new = new.join(i)
                    else:
                        new += i
                else:
                    break
            if new == "":
                return 0
            result = int(new)

        else:
            return 0

        INT_MIN = -2**31
        INT_MAX = 2**31 - 1

        if result < INT_MIN:
            return INT_MIN
        if result > INT_MAX:
            return INT_MAX

        return result