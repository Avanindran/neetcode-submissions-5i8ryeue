#include <unordered_set>

class Solution {
public:
    int longestConsecutive(vector<int>& nums) {

        unordered_set<int> numSet(nums.begin(), nums.end());
        int max_count = 0;
        //iterate through and update

        for (int num : nums) 
        {
            if (!numSet.count(num - 1)) 
            {
                int length = 1;
                while (numSet.count(num + length))
                {
                    length += 1;

                }
                max_count = max(max_count, length);
            }
        }
        return max_count;
                


    }
};
