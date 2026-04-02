from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        #counter dict
        seen = Counter(nums)

        #most common k returns list of tuples: [(num1, freq1), (num2, freq2)..]

        top_k = seen.most_common(k)

        return [num for num, freq in top_k]