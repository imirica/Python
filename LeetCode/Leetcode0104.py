class Solution:
    def maxDepth(self, root):
        if root is None:
            return 0
        else:
            leftDepth = self.maxDepth(root.left)
            rightDepth = self.maxDepth(root.right)
            return max(leftDepth, rightDepth) + 1
