class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # nums.sort()

        # seen = {}
        # ans = []
        # for i, num in enumerate(nums):
        #     target = 0 - num
        #     start = i + 1
        #     end = len(nums) - 1

        #     while start < end :
        #         if nums[start] + nums[end] < target:
        #             start += 1
                
        #         elif nums[start] + nums[end] > target:
        #             end -= 1
                
        #         elif nums[start] + nums[end] == target:
        #             if [num, nums[start], nums[end]] not in ans:
        #                 ans.append([num, nums[start], nums[end]])
        #             start += 1
        #         else:
        #             continue
        

        # return ans

        #use a two pointer approach and a linear pass
        nums.sort()
        ans = []
        
        for i, num in enumerate(nums):

            target = 0 - num
            start = i + 1
            end = len(nums) - 1

            while start < end:
                num1 = nums[start]
                num2 = nums[end]
                if num1 + num2 == target:
                    if [num, num1, num2] not in ans:
                        ans.append([num, num1, num2])
                    start += 1
                elif num1 + num2 > target:
                    end -= 1

                else:
                    start += 1
            
        return ans
                    




















        