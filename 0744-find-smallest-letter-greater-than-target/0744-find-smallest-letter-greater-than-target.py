class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        s = ord(target)
        for ch in letters:
            if ord(ch) > s:
                return ch
        return letters[0]