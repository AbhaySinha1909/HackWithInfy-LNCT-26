class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        n = len(arr)
        i = 0
        while i < n:
            if arr[i] == 0:
                # Only duplicate if there's room
                if i + 1 < n:
                    # Shift elements to the right
                    for j in range(n - 1, i + 1, -1):
                        arr[j] = arr[j - 1]
                    arr[i + 1] = 0
                i += 2  # Skip over the duplicated zero
            else:
                i += 1
