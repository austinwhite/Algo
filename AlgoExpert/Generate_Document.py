# Time Complexty: O(n*m) where n=len(characters) and m=len(document)
# Space Complexty: 0(n) where n=len(characters)

def generateDocument(characters, document):
    character_pool = {}

    for char in characters:
        if char not in character_pool:
            character_pool[char] = 0
        character_pool[char] += 1

    for char in document:
        if char not in character_pool or character_pool[char] == 0:
            return False
        character_pool[char] -= 1

    return True
