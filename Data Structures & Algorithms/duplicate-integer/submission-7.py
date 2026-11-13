class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        # Create a set and then compare the length of the set and the initial array
        # False will mean that there is a duplicate

        copy = set(nums)
        return not (len(copy) == len(nums))
        