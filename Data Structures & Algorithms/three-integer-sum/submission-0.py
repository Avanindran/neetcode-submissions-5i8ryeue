class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        seen = {}
        ans = []
        for i, num in enumerate(nums):
            target = 0 - num
            start = i + 1
            end = len(nums) - 1

            while start < end :
                if nums[start] + nums[end] < target:
                    start += 1
                
                elif nums[start] + nums[end] > target:
                    end -= 1
                
                elif nums[start] + nums[end] == target:
                    if [num, nums[start], nums[end]] not in ans:
                        ans.append([num, nums[start], nums[end]])
                    start += 1
                else:
                    continue
        

        return ans





        