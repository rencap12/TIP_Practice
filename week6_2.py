# # Write a function to find the middle node of a singly linked list. If the linked list has an even number of nodes, return the second middle node.
# # Input: head = [1, 2, 3, 4, 5]
# # Output: Node with value 3
# # Input: head = [1, 2, 3, 4, 5, 6]
# # Output: Node with value 4

# # different speed pointers, need handle if the len is even
# # slow, fast -> return slow when fast or fast.next is None


# # if not head return

# class Node:
#    def __init__(self, value, next=None):
#        self.value = value
#        self.next = next

# def find_middle(head): # 1 2 3 4 5 6
#     if not head:
#         return None
    
#     slow = head
#     fast = head

#     while fast and fast.next:
#         fast = fast.next.next
#         slow = slow.next

#     return slow

# protein_head = Node('1', Node('2', Node('3', Node('4', Node('5', Node('6'))))))
# temp = find_middle(protein_head)
# print(temp.value)
# '''
# class Node:
#     def __init__(self, value, next=None):
#         self.value = value
#         self.next = next

# def is_circular(clues):
#     if not clues:
#         return False 

#     slow = clues 
#     fast = clues
    
#     while fast and fast.next:
#         fast = fast.next  # Move fast one step first
#         if fast == slow:
#             return True  # Cycle detected
#         fast = fast.next  
        
#     return False 

# # Example Usage:
# clue1 = Node("The stolen goods are at an abandoned warehouse")
# clue2 = Node("The mayor is accepting bribes")
# clue3 = Node("They dumped their disguise in the lake")
# clue1.next = clue2
# clue2.next = clue3
# clue3.next = clue1  

# print(is_circular(clue1))  
# '''

# class Node:
#     def __init__(self, value, next=None):
#         self.value = value
#         self.next = next

# def collect_false_evidence(evidence):
#     if not evidence:
#         return []

#     slow = evidence
#     fast = evidence
#     inCycle = []
#     startNode = None  # marks the start of th

#     while fast and fast.next:
#         if startNode is None:
#             slow = slow.next
#             fast = fast.next.next
#             if fast == slow:
#                 startNode = slow
#         if startNode:
#             inCycle.append(slow.value)
#             slow = slow.next
#         if slow == startNode:
#             return inCycle

#     return inCycle # might be O(n^2) It was nice working with you!
#     # NIce implementation! thank you - would love to connect: https://www.linkedin.com/in/renecacapuno/