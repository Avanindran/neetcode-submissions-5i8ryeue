class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        seen = []
        high = 0

        start = 0
        end = 0
        while end < len(s) and start < len(s):

            if s[end] not in seen:
                seen.append(s[end])
                end += 1

            
            elif s[end] in seen:
                seen.clear()
                start += 1
                end = start
                

            high = max(high, len(seen))
        
        return high

        
