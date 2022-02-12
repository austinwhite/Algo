# Time: O(log(n)) where n is the length of array
# Space: O(n) where n is the length of array
def sortedSquaredArray(array):
    array.sort(key=abs)
    return [x*x for x in array]

# Time: O(n) where n is the length of array
# Space: O(n) where n is the length of array
def sortedSquaredArray(array):
    sorted_array = [0 for _ in range(len(array))]
    left = 0
    right = len(array)-1

    for i in reversed(range(len(array))):
        if abs(array[left]) < abs(array[right]):
            sorted_array[i] = array[right]**2
            right -= 1
        else:
            sorted_array[i] = array[left]**2
            left += 1

    return sorted_array
