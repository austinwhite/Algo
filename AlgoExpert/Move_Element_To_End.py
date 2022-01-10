# Time: O(n) where n=len(array)
# Space: O(1)

def moveElementToEnd(array, toMove):
    left = 0
    right = len(array)-1

    while left < right:
        if array[left] != toMove:
            left += 1
        elif array[right] == toMove:
            right -= 1
        else:
            array[left], array[right] = array[right], array[left]

    return array
