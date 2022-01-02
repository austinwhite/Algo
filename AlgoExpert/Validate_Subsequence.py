# Time Complexty: Linear, O(n) where n is the length of array
# Space Complexty: Constant, 0(1)

def isValidSubsequence(array, sequence):
    index = 0
	
    for value in array:
        if index == len(sequence):
            break
        if value == sequence[index]:
            index += 1
			
    return index == len(sequence)