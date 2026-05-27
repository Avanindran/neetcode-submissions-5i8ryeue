class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #cant sort, naive solution is to nested for loop and keep updating

        ans = 0

        for i, height in enumerate(heights):
           

            for j in range(i + 1, len(heights)):
                new = (j - i) * min(heights[j], height)
                ans = max(new, ans)
            
        
        return ans

        