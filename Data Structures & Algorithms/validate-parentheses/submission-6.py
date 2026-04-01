class Solution:
    def isValid(self, s: str) -> bool:


        maps = {'(': ')', '{' : '}', '[':']'}
        #stack
        starting = []
        for i in range(len(s)):
            
            if s[i] in maps.keys():
                starting.append(s[i])

            elif len(starting) == 0 and s[i] in maps.values():
                return False
            
            elif s[i] in maps.values() and s[i] == maps[starting[-1]]:
                del starting[-1]
            
            else:
                return False

        return not starting




        