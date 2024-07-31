from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def invertTree(root: Optional[TreeNode]) -> Optional[TreeNode]:
    if root is None:
        return None

    root.left, root.right = root.right, root.left

    invertTree(root.left)
    invertTree(root.right)

    return root



one = TreeNode(1)
three = TreeNode(3)
two = TreeNode(2, left=one, right=three)

t = invertTree(two)

print(t.val)
print(t.left.val)
print(t.right.val)
