import math
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        #Naive solution would be some kind of nested loop to check all
        count = -math.inf

        start = 0
        end = len(nums) - 1

        while start < len(nums):

            for j in range(len(nums) - 1, start - 1, -1):
                curr = sum(nums[start: j + 1])
                count = max(curr, count)
            
            start += 1


        return count

        



        