from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        arr = []
        for letter in t:
            arr.append(letter)

        if len(t) != len(s):
            return False
        for char in s:
            if char in arr:
                arr.remove(char)
            else:
                return False
        return len(arr) == 0

        