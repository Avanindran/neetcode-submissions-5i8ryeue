class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        #Linear pass

        intervals = sorted(intervals, key = lambda x: x[0])
        sol = []
        start, end = 0, 1


        for i, interval in enumerate(intervals):
            if len(sol) == 0:
                sol.append(interval)
            
            elif interval[start] > sol[-1][end]:
                sol.append(interval)
            
            else:
                sol[-1][end] = max(interval[end], sol[-1][end])


        return sol 

        