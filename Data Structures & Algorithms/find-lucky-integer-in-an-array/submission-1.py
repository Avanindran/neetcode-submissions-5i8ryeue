from collections import Counter
class Solution:
    def findLucky(self, arr: List[int]) -> int:

        seen = Counter(arr)

        lucky = -1
        for key in seen:

            if seen[key] == key and key > lucky :
                lucky = key

        
        return lucky


        