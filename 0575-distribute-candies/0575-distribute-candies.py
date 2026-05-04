class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        unique_types = len(set(candyType))
        
        limit = len(candyType) // 2
        
        return min(unique_types, limit)