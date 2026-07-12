class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        arr_dict = sorted(set(arr))
        result = {num : i+1 for i, num in enumerate(arr_dict)}
        answer = [result[num] for num in arr]
        return answer