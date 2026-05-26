class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        #binary search

        new_start = newInterval[0]
        new_end = newInterval[1]
        #base case
        if len(intervals) == 0:
            return [newInterval]

        left = 0
        right = len(intervals) - 1
        
        while left <= right:
            mid = (left + right) // 2

            if intervals[mid][0] < new_start:
                left = mid + 1
            
            else:
                right = mid - 1
        
        intervals.insert(left, newInterval)
        sol = []

        for interval in intervals:
            if not sol:
                sol.append(interval)
            elif interval[0] > sol[-1][1]:
                sol.append(interval)
            else:
                sol[-1] = [min(interval[0], sol[-1][0]), max(interval[1], sol[-1][1])]
            
        return sol



    
            

        



