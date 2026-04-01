import collections
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        first_non_zero = 0

        for i, num in enumerate(nums):
            if num != 0:
                nums[i] = nums[first_non_zero]
                nums[first_non_zero] = num
            
                first_non_zero += 1

        return nums
