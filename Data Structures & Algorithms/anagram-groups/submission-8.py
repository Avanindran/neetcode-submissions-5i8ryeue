class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        #dictionary
        store = {}


        for i, word in enumerate(strs):

            if tuple(sorted(word)) in store:
                store[tuple(sorted(word))].append(word)
            
            else:
                store[tuple(sorted(word))] = [word]
        

        return [word for word in store.values()]
        