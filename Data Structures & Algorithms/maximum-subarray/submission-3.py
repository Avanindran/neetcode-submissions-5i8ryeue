import math
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        #Naive solution would be some kind of nested loop to check all
        #idea is to rolling sum and when it turns negative that becomes new start point

        max_sum = nums[0]
        current = 0

        for num in nums:

            if current < 0:
                current = 0
            
            current += num

            max_sum = max(max_sum, current)

        
        return max_sum

        





        



        