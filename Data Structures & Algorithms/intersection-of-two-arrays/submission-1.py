class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:

        seen = set()
        sol = []
        for num in nums1:
            seen.add(num)
        
        for num in nums2:
            if num in seen:
                seen.remove(num)
                sol.append(num)
        return sol