class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        sol = []
        start, end = 0, k - 1

        while end < len(nums):

            sol.append(max(nums[start: end + 1]))

            end += 1
            start += 1
        
        return sol
        