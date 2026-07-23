class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort(key=lambda x: x[0]) 
        result = [intervals[0]]
        for i in intervals[1:]:
            if i[0] <= result[-1][1]: 
                result[-1][1] = max(result[-1][1], i[1])
            else:
                result.append(i)

        return result