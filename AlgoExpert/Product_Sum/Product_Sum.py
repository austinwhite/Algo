# Time: O(n) where n is the length of array
# Space: O(d) where d is the greatest depth of sub lists
def productSum(array, level=1):
    total = 0
    for item in array:
        if type(item) == list:
            total += productSum(item, level+1)
        else:
            total += item
    return total * level
