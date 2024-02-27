

class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def printLeafNodes(root):
    if root is not None:
        if root.left is None and root.right is None:
            print(root.key)
        else:
            printLeafNodes(root.left)
            printLeafNodes(root.right)

def countEdges(root):
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return 0
    return 1 + countEdges(root.left) + countEdges(root.right)

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

print("Leaf nodes:")
printLeafNodes(root)

print("\nNumber of edges:")
print(countEdges(root))