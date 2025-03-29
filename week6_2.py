# Write a function to find the middle node of a singly linked list. If the linked list has an even number of nodes, return the second middle node.
# Input: head = [1, 2, 3, 4, 5]
# Output: Node with value 3
# Input: head = [1, 2, 3, 4, 5, 6]
# Output: Node with value 4

# different speed pointers, need handle if the len is even
# slow, fast -> return slow when fast or fast.next is None


# if not head return

class Node:
   def __init__(self, value, next=None):
       self.value = value
       self.next = next

def find_middle(head): # 1 2 3 4 5 6
    if not head:
        return None
    
    slow = head
    fast = head

    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next

    return slow

protein_head = Node('1', Node('2', Node('3', Node('4', Node('5', Node('6'))))))
temp = find_middle(protein_head)
print(temp.value)