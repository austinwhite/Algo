# Time Complexty: Linear, O(n) where n is the length of array
# Space Complexty: Linear, 0(n) where n in the length of array

def twoNumberSum(array, targetSum):
    compliments = {}
	
    for value in array:
        if compliments.get(value):
            return [value, compliments[value]]
        else:
            compliments[targetSum-value] = value

    return []
