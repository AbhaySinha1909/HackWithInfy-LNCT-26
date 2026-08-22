class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        i , j = 0, 0
        n, m = len(firstList), len(secondList)
        intersec = []

        while i < n and j < m:
            start1, end1 = firstList[i][0], firstList[i][1]
            start2, end2 = secondList[j][0], secondList[j][1]

            s = max(start1, start2)
            e = min(end1, end2)
            if s <= e:
                intersec.append([s, e])
            if end1 <= end2:
                i += 1
            
            else:
                j += 1

        return intersec 