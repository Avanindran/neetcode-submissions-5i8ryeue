class Solution:
    def isValid(self, s: str) -> bool:


        maps = {'(': ')', '{' : '}', '[':']'}

        close_to_open = {')' : '(', '}' : '{', ']' : '['}
        #stack
        stack = []

        for char in s:

            if char in close_to_open:

                if stack and close_to_open[char] == stack[-1]:
                    stack.pop()
                
                else:
                    return False
            else:
                stack.append(char)
        
        return not stack




        