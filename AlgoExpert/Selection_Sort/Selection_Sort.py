# Time: Best/Average/Worst: O(n^2)
# Space: Best/Avererage/Worst: O(n^2)
def selectionSort(array):
	for i in range(len(array)):
		curr = i
		smallest = i
		for j in range(i, len(array)):
			if array[j] < array[smallest]:
				smallest = j
		swap(curr, smallest, array)
	return array

def swap(i, j, array):
	array[i], array[j] = array[j], array[i]
