class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        #two pointer approach

        arr = []

        for i, num in enumerate(nums):
            arr.append([num, i])
        
        arr.sort()
        start, end = 0, len(nums) - 1
        while start < end:
            if arr[start][0] + arr[end][0] > target:
                end -= 1
            elif arr[start][0] + arr[end][0] < target:
                start += 1

            else:
                return [min(arr[start][1], arr[end][1]), max(arr[end][1], arr[start][1])]