class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def in_order_traversal(root):
    if not root:
        return []

    result = []
    stack = []

    current = root

    while current or stack:
        # Traverse to the leftmost node while pushing nodes into the stack
        while current:
            stack.append(current)
            current = current.left

        # Pop the top node from the stack and process its value
        current = stack.pop()
        result.append(current.val)

        # Move to the right child to continue the inorder traversal
        current = current.right

    return result
