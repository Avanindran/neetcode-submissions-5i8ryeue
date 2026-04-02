class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        queue = []

        for num in nums:
            if len(queue) < k:
                queue.append(num)
            
            elif num > min(queue):
                queue[queue.index(min(queue))] = num

            else:
                continue
        
        return min(queue)
                

        
        