class Solution:
    def reverseParentheses(self, s: str) -> str:
        stk = []
        n = len(s)

        for i in range(n):
            if s[i] == ')':    
                result = []
                while stk and stk[-1] != "(":
                    a = stk.pop()
                    result.append(a)
                stk.pop()     
                stk.extend(result)
            
            else:
                stk.append(s[i])

        return ''.join(stk)
            