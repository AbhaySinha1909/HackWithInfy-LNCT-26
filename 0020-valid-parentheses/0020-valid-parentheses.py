class Solution:
    def isValid(self, s: str) -> bool:
        track = {")" : "(", "}":"{", "]": "["}
        stack = []
        for ch in s:
            if ch in "[{(":
                stack.append(ch)
            else:
                if len(stack) > 0 and stack[-1] == track[ch]:
                    stack.pop()
                else:
                    stack.append(ch)
        return not stack