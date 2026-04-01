import collections
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        last = len(nums) - 1
        while last >= 0 and nums[last] == 0:
            last -= 1

        i = 0
        while i < last:

            if nums[i] == 0:
                # Shift elements left to maintain relative order
                for j in range(i, last):
                    nums[j] = nums[j+1]
                nums[last] = 0
                
                while last >= 0 and nums[last] == 0:
                    last -= 1
            else:
                i += 1
        
        return nums
