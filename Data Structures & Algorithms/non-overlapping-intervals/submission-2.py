class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        #first sort by start
        intervals = sorted(intervals, key = lambda x: x[0])

        count = 0
        stack = []
        start, end = 0, 1

        for i, interval in enumerate(intervals):

            if len(stack) == 0:
                stack.append(interval)
            elif interval[start] >= stack[-1][end]:
                stack.append(interval)
            elif interval[end] < stack[-1][end]:
                count += 1
                stack[-1] = interval
            else:
                count += 1

        return count

        