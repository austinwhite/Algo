# Time: O(n) where n is the number of nodes
# Space: O(n) where n is the number of nodes

# This is the class of the input root. Do not edit it.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def branchSums(root):
    sums = []
    branchSumsHelper(root, sums)
    return sums

def branchSumsHelper(root, sums, curr_sum=0):
    if root is None:
        return
    curr_sum += root.value
    if root.left is None and root.right is None:
        sums.append(curr_sum)
    branchSumsHelper(root.left, sums, curr_sum)
    branchSumsHelper(root.right, sums, curr_sum)
