// Time: O(n) where n=numbers.size()
// Space: O(1)

class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        int left = 0;
        int right = numbers.size()-1;
        vector<int> match;
        
        while (left < right) {
            int test = numbers[left] + numbers[right];
            
            if (test == target) {
                break;
            } else if (test < target) {
                left++;
            } else {
                right--;
            }
        }
        
        match.push_back(left+1);
        match.push_back(right+1);
        return match;
    }
};