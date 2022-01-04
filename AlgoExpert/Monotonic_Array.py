# Time Complexty: O(n) where n=len(array)
# Space Complexty: 0(1)

def isMonotonic(array):
    not_ascending = True
    not_descending = True

    for i in range(1, len(array)):
        curr = array[i]
        prev = array[i-1]

        if prev < curr:
            not_ascending = False
        if curr < prev:
            not_descending = False

    return not_ascending or not_descending
