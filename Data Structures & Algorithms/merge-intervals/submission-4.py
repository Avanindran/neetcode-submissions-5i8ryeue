class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort()
        ret = []
        i = 0
        while i < len(intervals):

            if not ret or ret[-1][1] < intervals[i][0]:
                ret.append(intervals[i])
                i += 1
                
            else:
                
                ret[-1][1] = max(ret[-1][1], intervals[i][1])
                i += 1

                
            
               
        return ret


        