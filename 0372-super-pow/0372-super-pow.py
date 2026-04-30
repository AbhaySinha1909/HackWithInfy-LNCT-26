class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        from typing import List
        MOD = 1337
        def mod_pow(x: int, n: int) -> int:
            res = 1
            x %= MOD
            while n:
                if n % 2:
                    res = (res * x) % MOD
                x = (x * x) % MOD
                n //= 2
            return res
        
        def helper(b: List[int]) -> int:
            if not b:
                return 1
            last = b.pop()
            return (mod_pow(helper(b), 10) * mod_pow(a, last)) % MOD
        
        return helper(b)