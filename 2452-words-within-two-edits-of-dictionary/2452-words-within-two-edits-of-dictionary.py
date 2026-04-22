class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        ans  = []
        for word1 in queries:
            for word2 in dictionary:
                diff = sum(c1 != c2 for c1, c2 in zip(word1, word2))
                if diff <= 2:
                    ans.append(word1)
                    break
        return ans