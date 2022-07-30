#implement a single linked list

class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

class SLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    # insert in Linked List
    def insertSLL(self, value, location):
        newNode = Node(value)
        if self.head is None:  #if the LL has no node, reference the head and the tail to the note
            self.head = newNode
            self.tail = newNode
        else:
            if location == 0:  # if the location is '0', means we want to insert a new element at the beginning of the LL
                newNode.next = self.head #this is done because head stores first node physical location; Practically you are setting the new nod's first reference to the 1st node physical location
                self.head = newNode #we are updating head with new node physical location
            elif location == 1: #insert the element at the end
                newNode.next = None
                self.tail.next = newNode #the tail stores the physical location of the last node, so the tail will store now the newNode physical location; that's how you create reference to the last node
                self.tail = newNode #the tail points to the last node and it stores its value
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next # here the temp node is located on the position 'location-1' and it is the current node, so nextNode has to be tempNode.next -on the position 'location'
                tempNode.next = newNode # here the newNode is inserted at the 'location'
                newNode.next = nextNode # the newNode will point to the nextNode
