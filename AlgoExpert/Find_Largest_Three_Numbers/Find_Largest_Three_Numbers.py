# Time: O(n) where n=len(array)
# Space: O(1)

def findThreeLargestNumbers(array):
    first = float('-inf')
    second = float('-inf')
    third = float('inf')

    for value in array:
        if value > first:
            third = second
            second = first
            first = value
        elif value > second:
            third = second
            second = value
        elif value > third:
            third = value

    return [third, second, first]
