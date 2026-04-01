class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:


        sol = []
        for i in range(len(nums)):
            arr = nums.copy()
            arr.pop(i)
            count = 1
            for num in arr:
                count = count * num
            
            sol.append(count)
        

        return sol

        