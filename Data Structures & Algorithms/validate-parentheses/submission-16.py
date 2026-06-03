class Solution:
    def isValid(self, s: str) -> bool:
        mappings = {')': '(', '}': '{', ']': '['}
        stack = []
        for i in s:
            if i in mappings:
                if not stack or mappings[i] != stack[-1]:
                    return False
                stack.pop()
            else:
                stack.append(i)
        return not stack # True if stack is empty, False if stack isn't empty

        