class Solution:
    def isValid(self, s: str) -> bool:
        #implement a stack DS 
        stack = []
        res = { '(':')', '{':'}', '[':']'}
        
        for char in s:
            if len(stack) == 0:
                if char in res:
                    stack.append(char)
                else:
                    return False
            elif char in res:
                stack.append(char)
            elif res[stack[-1]] == char:
                stack.pop()
            else:
                return False

        return len(stack) == 0