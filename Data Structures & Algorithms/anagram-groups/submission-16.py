
from collections import defaultdict
class Solution:

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # create a dictionary of tuple(anagram) : list pairs

        sublists = defaultdict(list)

        for string in strs:

            sorted_string = "".join(sorted(string))

            sublists[sorted_string].append(string)

        return list(sublists.values())

        