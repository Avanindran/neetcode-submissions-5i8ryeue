from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        #counter dict
        seen = Counter(nums)

        #sort by descending frequency
        new_dict = dict(sorted(seen.items(), key = lambda item: item[1], reverse = True))

        #make a list of the first k most frequent and then reverse the list to be returned
        sol = list(new_dict.keys())[:k][::-1]

        return sol
