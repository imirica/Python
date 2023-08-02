# Definition of a ListNode class used to create linked list nodes
class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val 
        self.next = next 

# Function to remove duplicates from a sorted linked list
def remove_duplicates(head):
    if not head:  # If the linked list is empty (head is None), return it as it is
        return head
    
    current = head  # Initialize a pointer 'current' to the head of the linked list
    while current.next:  # Traverse the linked list until the last node (current.next is not None)
        if current.val == current.next.val:  # Check if the current node's value is the same as the next node's value
            current.next = current.next.next  # If they are the same, skip the next node by updating 'next' pointer of the current node
        else:
            current = current.next  # If they are different, move 'current' pointer to the next node

    return head  # Return the modified head of the linked list after removing duplicates
