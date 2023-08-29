# Definition of TreeNode class
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Function to convert sorted array to balanced BST
def sorted_array_to_bst(nums):
    # Base case: If the input array is empty, return None
    if not nums:
        return None
    
    # Calculate the index of the middle element
    mid = len(nums) // 2
    
    # Create a new TreeNode with the middle element as its value
    root = TreeNode(nums[mid])
    
    # Recursively construct the left subtree with elements before the middle element
    root.left = sorted_array_to_bst(nums[:mid])
    
    # Recursively construct the right subtree with elements after the middle element
    root.right = sorted_array_to_bst(nums[mid+1:])
    
    # Return the root of the constructed binary search tree
    return root

# Example usage
sorted_nums = [-10, -3, 0, 5, 9]
root = sorted_array_to_bst(sorted_nums)
