class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #two pointer approach

        left, right = 0, len(heights) - 1
        area = min(heights[left], heights[right]) * (right - left)

        while left <= right:

            area = max(area, min(heights[left], heights[right]) * (right - left))
            if heights[right] <= heights[left]:
                right -= 1
            else:
                left += 1
        
        return area

        