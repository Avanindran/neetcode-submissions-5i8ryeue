class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        
        running_max = nums[0]
        count = 0
        
        for num in nums:

            count += num
            running_max = max(count, running_max)
            if count < 0:
                count = 0

        return running_max 

            



        