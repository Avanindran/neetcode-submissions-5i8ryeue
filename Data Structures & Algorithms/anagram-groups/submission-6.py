
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        #hashmap to store the list of anagrams for each sorted string as index

        for char in strs:
            count = [0] * 26
            for c in char:
                count[ord(c) - ord('a')] += 1
            res[tuple(count)].append(char)
        
        return list(res.values())
        