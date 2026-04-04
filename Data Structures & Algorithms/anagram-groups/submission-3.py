from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        #use counting of alphabets to group anagrams

        res = defaultdict(list)


        for char in strs:

            #basically initialize an array and count instances of each character
            count = [0] * 26 #26 characters

            for s in char:
                
                count[ord(s) - ord('a')] += 1

            
            res[tuple(count)].append(char)
        

        return list(res.values())





 
        
