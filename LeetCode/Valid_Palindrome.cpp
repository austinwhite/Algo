// Time Complexty: Linear, O(n) where n is the length of s
// Space Complexty: Constant, 0(1)

class Solution {
private:
    bool sameChar(char a, char b) {
        if (isalpha(a) and isalpha(b)) {
            return tolower(a) == tolower(b);
        }
        else {
            return a == b;
        }
    }

public:
    bool isPalindrome(string s) {
        int left = 0;
        int right = s.length()-1;

        while (left < right) {
            char leftChar = s[left];
            char rightChar = s[right];

            if (!isalnum(leftChar)) {
                left++;
                continue;
            }
            else if (!isalnum(rightChar)) {
                right--;
                continue;
            }
            else {
                if (!sameChar(leftChar, rightChar)) {
                    return false;
                }
            }
            left++;
            right--;
        }
        return true;
    }
};