class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # Iterate through the list, store them in a seen dict as index : num pairs
        # Get the complement for each num, complement = target - num
        # Return [seen[complement], index]

        seen: dict[int, int] = {}
        for index, number in enumerate(nums):
            complement = target - number
            
            if complement in seen:
                return [seen[complement], index]
            # add to seen
            seen[number] = index
        raise ValueError("No pairs sum to target")



        