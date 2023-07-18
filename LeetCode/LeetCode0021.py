#Merge Two Sorted Lists

class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

def merge_two_lists(l1, l2):
    #create the first node from the merged list:
    merged_list = ListNode()
    current = merged_list

    #iterate through the lists until one becomes none
    while l1 and l2:
        #compare the value of the nodes from both lists
        if l1.val <= l2.val:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next

        #move the current pointer to the next node
        current = current.next

    #append the remaining nodes from the non-empty list
    if l1:
        current.next = l1
    else:
        current.next = l2

    return merged_list.next

# Example usage
# Create the first sorted list: 1 -> 2 -> 4
l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(4)

# Create the second sorted list: 1 -> 3 -> 4
l2 = ListNode(1)
l2.next = ListNode(3)
l2.next.next = ListNode(4)

# Merge the two lists
merged_list = merge_two_lists(l1, l2)

# Print the merged list: 1 -> 1 -> 2 -> 3 -> 4 -> 4
while merged_list:
    print(merged_list.val, end=" -> ")
    merged_list = merged_list.next

print("None")
