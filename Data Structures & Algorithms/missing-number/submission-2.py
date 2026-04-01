class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        
        seen = {}

        for i, n in enumerate(nums):
            
            seen[n] = i
        
        for i in range(0, len(nums) + 1):
            if i not in seen:
                return i
        
        return 0