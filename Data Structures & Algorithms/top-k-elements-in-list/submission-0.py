from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        seen = Counter(nums)


        new_dict = dict(sorted(seen.items(), key = lambda item: item[1], reverse = True))

        sol = list(new_dict.keys())[:k][::-1]

        return sol
