# Time: best: O(n) where n is the length of array
#       average: O(n^2) where n is the length of array
#       worst: O(n^2) where n is the length of array
# Space: O(1)
def bubbleSort(array):
    is_sorted = False
    while not is_sorted:
        is_sorted = True
        for bound in reversed(range(1, len(array))):
            for i in range(bound):
                if array[i+1] < array[i]:
                    is_sorted = False
                    array[i], array[i+1] = array[i+1], array[i]
    return array
