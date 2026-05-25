from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        maps = {}

        for word in strs:

            if tuple(sorted(word)) not in maps:
                maps[tuple(sorted(word))] = [word]
            else:
                maps[tuple(sorted(word))].append(word)
        
        return [word for word in maps.values()]

        