class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digit_to_char = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }

        if len(digits) < 1:
            return []

        result = []
    
        def backtrack(index, path):
            if index == len(digits):
                result.append("".join(path))
                return
            for char in digit_to_char[digits[index]]:
                backtrack(index + 1, path + [char])
        
        backtrack(0, [])
        return result