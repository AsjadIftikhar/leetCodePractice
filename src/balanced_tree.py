from typing import Optional


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def height(root):
    if root is None:
        return 0
    return 1 + max(height(root.left), height(root.right))


def isBalanced(root: Optional[TreeNode]) -> bool:
    if root is None:
        return True
    lh = height(root.left)
    rh = height(root.right)

    if abs(lh - rh) <= 1 and isBalanced(root.left) and isBalanced(root.right):
        return True

    return False

# Test is Balanced
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
print(isBalanced(root))  # True

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(2)
root.left.left = TreeNode(3)
root.left.right = TreeNode(3)
root.left.left.left = TreeNode(4)
root.left.left.right = TreeNode(4)
print(isBalanced(root))  # False

