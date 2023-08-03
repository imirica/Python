"""1st approach with in order traversal"""

def same_tree(root1, root2):
    if not root1 and not root2:
        return True  # Both trees are empty, so they are equal
    elif not root1 or not root2:
        return False  # One of the trees is empty, so they are not equal

    stack1 = []
    stack2 = []

    current1 = root1
    current2 = root2

    while current1 or stack1 or current2 or stack2:
        while current1 or current2:
            if not current1 or not current2:
                return False  # One of the trees has fewer nodes, so they are not equal

            stack1.append(current1)
            stack2.append(current2)

            current1 = current1.left
            current2 = current2.left

        current1 = stack1.pop()
        current2 = stack2.pop()

        if current1.val != current2.val:
            return False  # Nodes in the trees have different values, so they are not equal

        current1 = current1.right
        current2 = current2.right

    return True  # Both trees have the same structure and values, so they are equal


"""using recursion"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def same_tree(root1, root2):
    if not root1 and not root2:
        return True  # Both trees are empty, so they are equal
    elif not root1 or not root2:
        return False  # One of the trees is empty, so they are not equal

    if root1.val != root2.val:
        return False  # Nodes in the trees have different values, so they are not equal

    return same_tree(root1.left, root2.left) and same_tree(root1.right, root2.right)

