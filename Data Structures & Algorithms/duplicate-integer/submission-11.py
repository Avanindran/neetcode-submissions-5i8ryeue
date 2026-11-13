class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        # Create a set and then compare the length of the set and the initial array
        # False will mean that there is a duplicate

        seen = set()
        
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        
        return False
        