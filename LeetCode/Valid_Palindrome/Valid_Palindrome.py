# Time: O(n)
# Space: O(1)

class Solution:
    def validchar(self, c: chr) -> bool:
        return c.isalnum()

    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s)-1
        s = s.lower()

        while left < right:
            if not self.validchar(s[left]):
                left += 1
            elif not self.validchar(s[right]):
                right -= 1
            else:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1

        return True
