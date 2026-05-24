class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        

        rolling_max = nums[0]
        cur_max, cur_min = 1, 1

        for num in nums:
            temp = cur_max * num
            cur_max = max(num * cur_max, num * cur_min, num)
            cur_min = min(num, temp, cur_min * num)

            rolling_max = max(cur_max, rolling_max)
        
        return rolling_max
