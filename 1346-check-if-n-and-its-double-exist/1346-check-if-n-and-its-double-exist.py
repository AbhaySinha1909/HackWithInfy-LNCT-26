class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        arr.sort()
        i, j = 0, 1
        while j < len(arr):
            if arr[j] == 2 * arr[i]:
                return True
            elif arr[j] < 2 * arr[i]:
                j += 1
            else:
                i += 1
                if i == j:  
                    j += 1
        return False