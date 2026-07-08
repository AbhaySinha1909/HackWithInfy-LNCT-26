from typing import List

class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        MOD = 10**9 + 7
        n = len(s)

        prefix_sum = [0] * (n+1)
        prefix_num = [0] * (n+1)
        prefix_count = [0] * (n+1)
        pow10 = [1] * (n+1)

        # precompute powers of 10
        for i in range(1, n+1):
            pow10[i] = (pow10[i-1] * 10) % MOD

        # build prefix arrays
        for i in range(1, n+1):
            d = int(s[i-1])
            prefix_sum[i] = prefix_sum[i-1]
            prefix_num[i] = prefix_num[i-1]
            prefix_count[i] = prefix_count[i-1]
            if d != 0:
                prefix_sum[i] = (prefix_sum[i-1] + d) % MOD
                prefix_num[i] = (prefix_num[i-1] * 10 + d) % MOD
                prefix_count[i] = prefix_count[i-1] + 1

        answer = []
        for l, r in queries:
            # sum of digits
            sum_curr = (prefix_sum[r+1] - prefix_sum[l]) % MOD

            # count of digits
            k = prefix_count[r+1] - prefix_count[l]

            if k == 0:
                answer.append(0)
                continue

            # concatenated number modulo
            num_mod = (prefix_num[r+1] - prefix_num[l] * pow10[k]) % MOD
            num_mod = (num_mod + MOD) % MOD  # ensure non-negative

            result = (sum_curr * num_mod) % MOD
            answer.append(result)

        return answer
