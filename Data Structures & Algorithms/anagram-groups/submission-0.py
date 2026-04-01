class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        #implement set to string hash

        seen = {}
        sol = []
        for i, char in enumerate(strs):

            if tuple(sorted(char)) in seen.keys():
                seen[tuple(sorted(char))].append(char)
            else:
                seen[tuple(sorted(char))] = [char]
            
        
        for val in seen.values():
            sol.append(val)
        

        return sol
                
        
