class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for i, n in enumerate(nums):

            if n in nums[i+1:len(nums)]:
                return True
        
        return False