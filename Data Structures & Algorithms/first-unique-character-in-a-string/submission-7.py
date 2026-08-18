from collections import Counter
class Solution:
    def firstUniqChar(self, s: str) -> int:

        count = defaultdict(int)
        n = len(s)

        for i, c in enumerate(s):

            if c not in count:
                count[c] = i
            else:
                count[c] = n 
        
        for c in count:
            if count[c] != n:
                return count[c]
        
        return -1
        
    




        