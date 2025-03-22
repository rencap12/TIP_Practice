# # # # # # class Villager:
# # # # # #     def __init__(self, name, species, catchphrase):
# # # # # #         self.name = name
# # # # # #         self.species = species
# # # # # #         self.catchphrase = catchphrase
# # # # # #         self.friends = []

# # # # # #     def get_mutuals(self, new_contact):
# # # # # #         # go through self friends see if in new contact's friends, append to ret
# # # # # #         mutuals = []
# # # # # #         for i in self.friends:
# # # # # #             if i in new_contact.friends:
# # # # # #                 mutuals.append(i.name)
# # # # # #         return mutuals
    
# # # # # # bob = Villager("Bob", "Cat", "pthhhpth")
# # # # # # marshal = Villager("Marshal", "Squirrel", "sulky")
# # # # # # ankha = Villager("Ankha", "Cat", "me meow")
# # # # # # fauna = Villager("Fauna", "Deer", "dearie")
# # # # # # raymond = Villager("Raymond", "Cat", "crisp")
# # # # # # stitches = Villager("Stitches", "Cub", "stuffin")

# # # # # # bob.friends = [stitches, raymond, fauna]
# # # # # # marshal.friends = [raymond, ankha, fauna]
# # # # # # print(bob.get_mutuals(marshal))

# # # # # # ankha.friends = [marshal]
# # # # # # print(bob.get_mutuals(ankha))

# # # # # class Node:
# # # # #     def __init__(self, value, next=None):
# # # # #         self.value = value
# # # # #         self.next = next

# # # # # # For testing
# # # # # def print_linked_list(head):
# # # # #     current = head
# # # # #     while current:
# # # # #         print(current.value)
# # # # #         current = current.next

# # # # # kk_slider = Node("K.K. Slider")
# # # # # harriet = Node("Harriet")
# # # # # saharah = Node("Saharah")
# # # # # isabelle = Node("Isabelle")

# # # # # saharah.next = isabelle
# # # # # harriet.next = saharah
# # # # # kk_slider.next = harriet

# # # # # print_linked_list(kk_slider)

# # # # class Node:
# # # #     def __init__(self, value, next=None):
# # # #         self.value = value
# # # #         self.next = next

# # # # # For testing
# # # # def print_linked_list(head):
# # # #     current = head
# # # #     while current:
# # # #         print(current.value)
# # # #         current = current.next

# # # # def add_first(head, task):
# # # #     # init the new head node w/ the task, the next of new head is head
# # # #     newNode = Node(task)
# # # #     newNode.next = head
# # # #     return newNode

# # # # task_1 = Node("shake tree")
# # # # task_2 = Node("dig fossils")
# # # # task_3 = Node("catch bugs")
# # # # task_1.next = task_2
# # # # task_2.next = task_3

# # # # # Linked List: shake tree -> dig fossils -> catch bugs
# # # # print_linked_list(add_first(task_1, "check turnip prices"))

# # # class Node:
# # #     def __init__(self, value, next=None):
# # #         self.value = value
# # #         self.next = next

# # # # For testing
# # # def print_linked_list(head):
# # #     current = head
# # #     while current:
# # #         print(current.value)
# # #         current = current.next

# # # def halve_list(head):
# # #     # init a curr node to traverse, as we go curr.value /= 2, return
# # #     curr = head
# # #     while curr:
# # #         temp = curr.value
# # #         x = float(temp) / 2
# # #         curr.value = x
# # #         curr = curr.next
        
# # #     return head
    
# # # node_one = Node(5)
# # # node_two = Node(6)
# # # node_three = Node(7)
# # # node_one.next = node_two
# # # node_two.next = node_three

# # # # Input List: 5 -> 6 -> 7
# # # print_linked_list(halve_list(node_one))

# # class Node:
# #     def __init__(self, value, next=None):
# #         self.value = value
# #         self.next = next

# # # For testing
# # def print_linked_list(head):
# #     current = head
# #     while current:
# #         print(current.value)
# #         current = current.next

# # def delete_tail(head):
# #     if head.next is None:
# #         return None
# #     # prev init to None in beginning, curr = head, if curr.next is None, prev.next = None
# #     prev = Node('')
# #     current = head
# #     while current:
# #         if current.next is None:
# #             prev.next = None
# #             break
# #         else:
# #             prev = current
# #             current = current.next
# #     return head

# # butterfly = Node("Common Butterfly")
# # ladybug = Node("Ladybug")
# # beetle = Node("Scarab Beetle")
# # butterfly.next = ladybug
# # ladybug.next = beetle

# # # Input List: butterfly -> ladybug -> beetle
# # print_linked_list(delete_tail(beetle))


# class Node:
#     def __init__(self, value, next=None):
#         self.value = value
#         self.next = next

# # For testing
# def print_linked_list(head):
#     current = head
#     while current:
#         print(current.value)
#         current = current.next

# def find_min(head):
#     # traverse, keep track of currMin, reassign if lower
#     low = float('inf')
#     while head:
#         if head.value < low:
#             low = head.value
#         head = head.next
#     return low

# head1 = Node(5, Node(6, Node(7, Node(8))))
# head2 = Node(8, Node(5, Node(6, Node(7))))

# # Linked List: 5 -> 6 -> 7 -> 8
# print(find_min(head1))

# # Linked List: 8 -> 5 -> 6 -> 7
# print(find_min(head2))


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

# For testing
def print_linked_list(head):
    current = head
    while current:
        print(current.value)
        current = current.next

def delete_item(head, item):
    # if curr.next is item.value then curr.next = curr.next.next
    if head.value == item:
        return head.next
    curr = head
    while curr.next:
        if curr.next.value == item:
            curr.next = curr.next.next
            break
        curr = curr.next
    
    return head if head is not None else "wack"

slingshot = Node("Slingshot")
peaches = Node("Peaches")
beetle = Node("Scarab Beetle")
slingshot.next = peaches
peaches.next = beetle

# Linked List: slingshot -> peaches -> beetle
print_linked_list(delete_item(slingshot, "Peaches"))
print('1')
# Linked List: slingshot -> beetle
print_linked_list(delete_item(slingshot, "Triceratops Torso"))
print('2')
print_linked_list(delete_item(beetle, "Scarab Beetle"))
print('3')
        