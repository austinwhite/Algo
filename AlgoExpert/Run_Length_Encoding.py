# Time Complexty: Linear, O(n) where n is the length of string
# Space Complexty: Linear, 0(n) where n in the length of string

def runLengthEncoding(string):
    encoded = ['1', string[0]]

    for char in string[1:]:
        prev_char = encoded[-1]
        count = int(encoded[-2])

        if char == prev_char:
            if count < 9:
                encoded[-2] = str(count + 1)
                continue
        encoded.append('1')
        encoded.append(char)

    return ''.join(encoded)
