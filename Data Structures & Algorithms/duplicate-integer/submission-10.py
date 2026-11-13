class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        # Create a set and then compare the length of the set and the initial array
        # False will mean that there is a duplicate

        unique_numbers = set()
        
        for num in nums:
            if num in unique_numbers:
                return True
            unique_numbers.add(num)
        
        return False
        