class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        result = []
        for i in range(left, right + 1):
            n = str(i)
            count = 0
            for j in range(len(n)):
                if n[j] != "0" and i%int(n[j]) == 0:
                    count += 1
                    if count == len(n):
                        result.append(i)
        return result

        