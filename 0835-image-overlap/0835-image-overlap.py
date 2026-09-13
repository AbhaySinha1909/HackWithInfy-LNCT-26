class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        n = len(img1)
        
        count1_of_1 = []
        count1_of_2 = []
        
        for r in range(n):
            for c in range(n):
                if img1[r][c] == 1:
                    count1_of_1.append((r, c))

                if img2[r][c] == 1:
                    count1_of_2.append((r, c))
    
        if img1 == img2:
            return len(count1_of_1)
        
        shift_count = Counter()
        max_freq_shift_count = 0
        for r1, c1 in count1_of_1:
            for r2, c2 in count1_of_2:
                shift = (r2 - r1, c2 - c1)
                shift_count[shift] += 1
                max_freq_shift_count = max(max_freq_shift_count, shift_count[shift])
        
        return max_freq_shift_count