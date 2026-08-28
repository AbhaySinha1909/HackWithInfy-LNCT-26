class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strss = sorted(strs)
        visited = []
        a = strss[0]
        b = strss[-1]
        for k in range(min(len(a), len(b))):
            if a[k] == b[k]:
                visited.append(a[k])
                k += 1
            else:
                break
        result = ''.join(map(str, visited))
        if len(visited) > 0:
            return result
        else:
            return ""