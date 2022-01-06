// Time Complexty: O(n) where n is the size of nums
// Space Complexty: O(n) where n is the size of nums

#include <unordered_map>

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        std::unordered_map<int, int> map;
        vector<int> pair;
        
        for (int i=0; i<nums.size(); i++) {
            int value = nums[i];
            if (map.find(value) == map.end()) {
                map[target-value] = i;
            } else {
                pair.push_back(map[value]);
                pair.push_back(i);
                return pair;
            }
        }
        return pair;
    }
};