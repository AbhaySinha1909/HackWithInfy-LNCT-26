class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        if len(intervals) == 0:
            return [newInterval]

        
        intervals.append(newInterval)
        intervals.sort(key=lambda x : x[0])

        merged = []
        start1, end1 = intervals[0][0], intervals[0][1]

        for i in range(1, len(intervals)):
            start2, end2 = intervals[i][0], intervals[i][1]

            if end1 >= start2:
                start1 = start1
                end1 = max(end1, end2)
                continue
            
            merged.append([start1, end1])
            start1 = start2
            end1 = end2
        
        if [start1, end1] not in merged:
            merged.append([start1, end1])
    
        return merged