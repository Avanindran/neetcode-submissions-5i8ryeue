class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        sol = [0] * (len(nums) - k + 1)
        start, end, i = 0, k - 1, 0

        while end < len(nums):

            sol[i] = max(nums[start: end + 1])

            i += 1
            end += 1
            start += 1
        
        return sol
        