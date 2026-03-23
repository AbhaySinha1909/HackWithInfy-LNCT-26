class Solution:
    def isPalindrome(self, s: str) -> bool:
        import re
        p = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        return p == p[::-1]