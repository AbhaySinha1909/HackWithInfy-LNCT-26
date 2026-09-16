class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        l_1, b_1 = abs(ax1 - ax2), abs(ay1 - ay2)
        l_2, b_2 = abs(bx1 - bx2), abs(by1 - by2)

        ar_1 = l_1 * b_1
        ar_2 = l_2 * b_2

        overlap_x1 = max(ax1, bx1)
        overlap_y1 = max(ay1, by1)
        overlap_x2 = min(ax2, bx2)
        overlap_y2 = min(ay2, by2)

        overlap_area = 0
        if overlap_x1 < overlap_x2 and overlap_y1 < overlap_y2:
            overlap_area = (overlap_x2 - overlap_x1) * (overlap_y2 - overlap_y1)


        total_area = ar_1 + ar_2 - overlap_area

        return total_area