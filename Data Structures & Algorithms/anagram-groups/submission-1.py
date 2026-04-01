class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        #implement set to string hash

        seen = {}
        
        for i, char in enumerate(strs):

            key = tuple(sorted(char))
            if key in seen:
                seen[key].append(char)
            else:
                seen[key] = [char]
            
        
        return list(seen.values())
        

 
        
