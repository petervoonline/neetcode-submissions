class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 0 or (len(s) % 2) == 1 or s[0] in {']','}',')'}:
            return False
        stack = []
        for i in s:
            if i in {'[','(','{'}:
                stack.append(i)
            else:
                if len(stack) == 0:
                    return False
                tmp = stack[-1] + i
                if tmp in {'[]','{}','()'}:
                    stack.pop()
                else:
                    return False
        if len(stack) > 0:
                return False
        return True

s="(){}}{"

        