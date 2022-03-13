# Time: O(n) where n is the number of digits in x
# Space: O(1)

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        original = x
        reverse = 0

        while x != 0:
            remainder = x % 10
            reverse = reverse * 10 + remainder
            x //= 10

        return reverse == original
