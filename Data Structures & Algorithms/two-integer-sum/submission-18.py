class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:


        
        #get a the complement and then find if it exists in the rest of the array
        # maintain a dictionary of index : value pairs
        seen = {}
        for i, num in enumerate(nums):
            
            
            complement = target - num

            if complement in seen:
                return [seen[complement], i]
            else:
                seen[num] = i



        