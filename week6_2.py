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





#iterative solution
#counting how many elements are in a list of strings
def count_suits_iterative(suits):
    count = 0
    for suit in suits:
        count += 1
    return count
    

#recursive solution
#counting how many elements are in a list of strings
def count_suits_recursive(suits):
    count = 0
    if len(suits) < 1:
        return count
    return 1 + count_suits_recursive(suits[:-1])



print(count_suits_iterative(["Mark I", "Mark II", "Mark III"]))
print(count_suits_recursive(["Mark I", "Mark I", "Mark III", "Mark IV"]))
print(count_suits_recursive(["Mark I", "Mark II", "Mark III", "Mark IV"]))


# Problem 1: Counting Iron Man's Suits
# #iterative solution
# #counting how many elements are in a list of strings
# def count_suits_iterative(suits):
#     count = 0
#     for suit in suits:
#         count += 1
#     return count
    

# #recursive solution
# #counting how many elements are in a list of strings
# def count_suits_recursive(suits):
#     count = 0
#     if len(suits) < 1:
#         return count
#     else:
#         return 1 + count_suits_recursive(suits[:-1])

# print(count_suits_iterative(["Mark I", "Mark II", "Mark III"]))
# print(count_suits_recursive(["Mark I", "Mark I", "Mark III", "Mark IV"]))


# Problem 2: Collecting Infinity Stones
# 5 + sum_stones([10, 15, 20, 25, 30])
# 5 + 10 + sum_stones([15, 20, 25, 30])
# 5 + 10 + 15 + sum_stones([20, 25, 30])
# 5 + 10 + 15 + 20 + sum_stones([25,30])
# 5 + 10 + 15 + 20 + 25 + sum_stsones([30])
# 5 + 10 + 15 + 20 + 25 + 30
# def sum_stones(stones):
#     # len(stones) == 1
#     if len(stones) == 1:
#         # return stones[0]
#         return stones[0]
#     # return stones[0] + sum_stones(stones[1:])
#     return stones[0] + sum_stones(stones[1:])

# print(sum_stones([5, 10, 15, 20, 25, 30]))
# print(sum_stones([12, 8, 22, 16, 10]))

# Guys if you like we can finished after the classes? -Roy
# What do you think?
# it was nice working with you guys!!!
# hi! i have to wake up early tomorrow so i cant tonight but! i think this document is open for 23 hours - so we can see our work!

#it was nice talking and working with you guys tooooo
# but i dont think i can stay after class sorry :( we can connect on slack or something mine should be my name - Sumanth
# Problem 3: Counting Unique Suits
# def count_suits_iterative(suits):
#     # for suits[0] not in suits: LMAOOOOOO rip, let me try finish this lol pray for me
#     #   if  
#     # can also use for loop - check if not exists: add to total - return total
#     return len(set(suits))

# def count_suits_recursive(suits): # WIP
#     # base: empty list -> return 0
   
# print(count_suits_iterative(["Mark I", "Mark II", "Mark III"]))
# print(count_suits_recursive(["Mark I", "Mark I", "Mark III"]))

def count_suits_recursive(suits):
    if not suits:  # Base case: empty list
        return 0
    first, rest = suits[0], suits[1:]
    rest_unique_count = count_suits_recursive([x for x in rest if x != first])  # Filter out duplicates of first
    return 1 + rest_unique_count  # Include first element in count

print('clear')
print(count_suits_recursive(["Mark I", "Mark I", "Mark III"]))