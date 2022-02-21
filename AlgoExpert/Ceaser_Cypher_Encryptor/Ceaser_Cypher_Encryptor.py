# Time: O(n) where n=len(string)
# Space: O(n) where n=len(string)

def caesarCipherEncryptor(string, key):
    rotated = [None] * len(string)

    for i in range(len(string)):
        offset = (((ord(string[i])) - ord('a')) + key) % 26
        rotated[i] = (chr(ord('a') + offset))

    return ''.join(rotated)
