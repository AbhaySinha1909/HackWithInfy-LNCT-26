class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        n = len(s)
        m = len(goal)
        if n != m:
            return False
        
        if s == goal:
            return n > len(set(s))
        
        diff = []
        for i in range(n):
            if s[i] != goal[i]:
                diff.append((s[i], goal[i]))
            
        return len(diff) == 2 and diff[0] == diff[1][::-1]