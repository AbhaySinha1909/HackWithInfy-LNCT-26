class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        res = []
        def backtrack(string):
            if len(string) == n:
                res.append(string)
                return
        
            for ch in ["a", "b", "c"]:
                if not string or string[-1] != ch:
                    backtrack(string + ch)
        backtrack("")
        return res[k-1] if len(res) >= k else ""