class Solution:
    def countPoints(self, rings: str) -> int:
        rod = 0
        for i in range(0, 10):
            count = 0
            if f"R{i}" in rings:
                count += 1
            if f"G{i}" in rings:
                count += 1
            if f"B{i}" in rings:
                count += 1
            
            if count == 3:
                rod += 1
        return rod