# Time Complexty: Linear, O(n) where n is the length of string
# Space Complexty: Linear, 0(n) where n in the length of string

def firstNonRepeatingCharacter(string):
    character_count = {}

    for char in string:
        if character_count.get(char):
            character_count[char] += 1
        else:
            character_count[char] = 1

    for i in range(len(string)):
        if character_count[string[i]] == 1:
            return i

    return -1
