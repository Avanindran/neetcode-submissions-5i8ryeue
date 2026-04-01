class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        sol = []

        for i, n in enumerate(nums):
            temp = abs(nums[i]) - 1
            if nums[temp] > 0:
                nums[temp] *= -1

        for i, n in enumerate(nums):

            if n > 0:
                sol.append(i + 1)
        
        return sol



