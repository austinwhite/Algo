# Time Complexty: Linear, O(n) where n is the length of string
# Space Complexty: Constant, 0(1)

def isPalindrome(string):
    left = 0
    right = len(string)-1

    while left < right:
        if string[left] != string[right]:
            return False
        left += 1
        right -= 1

    return True
