# Time: O(n) where n is the number of nodes
# Space: O(h) where h is the depth of tree

def nodeDepths(root):
    total_depths = get_node_depths(root, 0)
    return total_depths

def get_node_depths(root, curr_depth):
    if root is None:
        return 0
    left = get_node_depths(root.left, curr_depth+1)
    right = get_node_depths(root.right, curr_depth+1)
    return curr_depth + left + right

# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
