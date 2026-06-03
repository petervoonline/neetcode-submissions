class Solution:
    def isValid(self, s: str) -> bool:
        mappings = {')': '(', '}': '{', ']': '['}
        stack = []
        for i in s:
            if i in mappings:
                if len(stack) == 0 or mappings[i] != stack[-1]:
                    return False
                stack.pop()
            else:
                stack.append(i)
        if len(stack) > 0:
            return False
        return True


s="(){}}{"

        