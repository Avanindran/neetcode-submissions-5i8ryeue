class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        count = 0
        largest = 0
        unique = set(nums)
        iterator = nums.copy()
        done = set()


        for num in unique:
            if num - 1 in unique:
                continue
            count = 0
            end = num
            while end in unique:
                count += 1
                largest = max(largest, count)
                end += 1
        
        return largest
            


        