class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        
        nums.sort()
        seen = {}
        sol = []
        for i, n in enumerate(nums):
            seen[n] = i

        for i in range(1, len(nums) + 1):
            if i not in seen:
                sol.append(i)

        return sol