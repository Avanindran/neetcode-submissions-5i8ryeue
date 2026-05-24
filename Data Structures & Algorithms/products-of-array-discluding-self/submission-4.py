class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        #Naive solution is to use div operator, find total prod and div by cur_num
        total = 1
        zeros = 0
        ans = []
        for num in nums:
            if num != 0:
                total *= num
            else:
                zeros += 1
        
        for n in nums:
            if zeros > 1:
                ans.append(0)
            elif zeros == 1:
                if n == 0:
                    ans.append(total)
                else:
                    ans.append(0)
            
            else:
                ans.append(total // n)
            
        
        return ans

        