# Time: O(n)
# Space: O(1)
class Solution:
    def romanToInt(self, s: str) -> int:
        number = 0
        value = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }

        i = 0
        while i < len(s):
            curr = s[i]
            next = None

            if i+1 < len(s):
                next = s[i+1]
                
            if next and value[curr] < value[next]:
                number += value[next] - value[curr]
                i += 1
            else:
                number += value[curr]
            
            i += 1
                
        return number
