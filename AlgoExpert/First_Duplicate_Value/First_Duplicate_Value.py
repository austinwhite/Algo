# Time: O(n) where n=len(array)
# Space: O(n) where n=len(array)

def firstDuplicateValue(array):
    values = set()

    for value in array:
        if value not in values:
            values.add(value)
        else:
            return value

    return -1
