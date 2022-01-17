// Time: O(n) where n is equal to the number of digits in x
// Space: O(1)

class Solution {
public:
    bool isPalindrome(int x) {
        if (x < 0) {
            return false;
        }
        
        long original = x;
        long reversed = 0;
        while (x != 0) {
            int remainder = x % 10;
            reversed = reversed * 10 + remainder;
            x /= 10;
        }
        return reversed == original;
    }
};