class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #just use a set and then compare length of set to og array

        new = set(nums)
        return len(new) != len(nums)