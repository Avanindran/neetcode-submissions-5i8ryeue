

class Solution:
    from collections import defaultdict
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # create a dictionary of tuple(anagram) : list pairs

        sublists = defaultdict(list)

        for string in strs:

            sorted_string = sorted(string)

            sublists[tuple(sorted_string)].append(string)

        return [array for array in sublists.values()]

        