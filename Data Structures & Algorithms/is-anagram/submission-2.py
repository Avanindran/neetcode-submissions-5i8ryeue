from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False


        counts = Counter(s)

        for char in t:

            counts[char] -= 1
        
        for value in counts.values():
            if value != 0:
                return False

        return True
        