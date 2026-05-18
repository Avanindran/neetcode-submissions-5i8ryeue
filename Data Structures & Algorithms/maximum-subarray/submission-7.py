import math
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:



        # max_sum = nums[0]
        # current = 0

        # for num in nums:

        #     if current < 0:
        #         current = 0
            
        #     current += num

        #     max_sum = max(max_sum, current)

        
        # return max_sum


        #array cannot be sorted since it must be contiguous subarrs. 

        running_max = nums[0]

        for i, num in enumerate(nums):
            count = num
            running_max = max(running_max, count)
            for n in nums[i + 1: len(nums)]:
                count += n
            
                running_max = max(running_max, count)

        return running_max

        





        



        