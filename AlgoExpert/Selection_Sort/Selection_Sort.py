# Time: Best/Average/Worst: O(n^2)
# Space: Best/Avererage/Worst: O(n^2)
def selectionSort(array):
    curr = 0
    while curr < len(array) - 1:
        smallest = curr
        for i in range(curr + 1, len(array)):
            if array[smallest] > array[i]:
                smallest = i
        swap(curr, smallest, array)
        curr += 1
    return array

def swap(i, j, array):
    array[i], array[j] = array[j], array[i]
