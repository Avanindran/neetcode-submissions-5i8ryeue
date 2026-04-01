class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        sol = []

        intervals.append(newInterval)
        intervals.sort()

        i = 0
        while i < len(intervals):

            if len(sol) == 0 or intervals[i][0] > sol[-1][1]:
                sol.append(intervals[i])
                i += 1
            
            else:
                sol[-1] = [sol[-1][0], max(sol[-1][1], intervals[i][1])]
                i += 1
        
        return sol



