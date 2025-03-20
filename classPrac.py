# # # class Car:
# # #     def __init__(self):
# # #         self.test = "Hello"

# # #     def printHello(self):
# # #         print(self.test)


# # # bro = Car()
# # # bro.printHello()



# # # class Villager:
# # #     def __init__(self, name, species, catchphrase):
# # #         self.name = name
# # #         self.species = species
# # #         self.catchphrase = catchphrase
# # #         self.furniture = []

# # #     def greet_player(self, player_name):
# # #         return f"{self.name}: Hey there, {player_name}! How's it going, {self.catchphrase}!"


# # # apollo = Villager("Apollo", "Eagle", "pah")
# # # print(apollo.name)  
# # # print(apollo.species)  
# # # print(apollo.catchphrase) 
# # # print(apollo.furniture) 

# # # bones = Villager("Bones", "Dog", "yip yip")
# # # print(bones.greet_player("Bones"))

# # # bones.catchphrase = "ruff it up RAHAHHAHAHAHAAH"
# # # print(bones.greet_player("Bones"))




# # class Node:
# #     def __init__(self, value, next=None):
# #         self.value = value
# #         self.next = next


# # tom_nook = Node("Tom Nook")
# # tommy = Node("Tommy") 
# # tom_nook.next = tommy 
# # # print(tom_nook.value) 
# # # print(tom_nook.next.value) 
# # # print(tommy.value) 
# # # print(tommy.next) 

# # timmy = Node("Timmy")
# # tom_nook.next = timmy
# # timmy.next = tommy


# # # print(tom_nook.value)
# # # print(tom_nook.next.value)
# # # print(timmy.value)
# # # print(timmy.next.value)
# # # print(tommy.value)
# # # print(tommy.next)

# # # temp = Node("temp")
# # # temp.next = tom_nook
# # prev = Node("temp")
# # prev.next = tom_nook
# # curr = tom_nook

# # while curr:
# #     if curr.value == "Tom Nook":
# #         prev.next = curr.next
# #         curr.next = None
# #         break
# #     prev = curr
# #     curr = curr.next


# # saharah = Node("Saharah")
# # tommy.next = saharah


# # print(tom_nook.next) 
# # print(timmy.value) 
# # print(timmy.next.value)  
# # print(tommy.value) 
# # print(tommy.next.value)
# # print(saharah.value)  
# # print(saharah.next) 


# # isabelle = Node("Isabelle")
# # saharah = Node("Saharah")
# # cj = Node("C.J.")

# # isabelle.next = saharah
# # saharah.next = cj


# # def print_list(head):
# #     curr = head 
# #     joined = ""
# #     while curr:
# #         joined += curr.value + "->"
# #         curr = curr.next
    
# # #     return joined[:len(joined)-2]

# # # print(print_list(timmy))


# # class Player:
# #     def __init__(self, character, kart, opponent=None):
# #         self.character = character
# #         self.kart = kart
# #         self.items = []
# #         self.ahead = opponent
        
# # def get_rank(my_player):
# #     if not my_player.ahead:
# #         return 1
    
# #     curr = my_player
# #     count = 1
# #     while curr.ahead:
# #         curr = curr.ahead
# #         count += 1

# #     return count

# # peach = Player("Peach", "Daytripper")
# # mario = Player("Mario", "Standard Kart M", peach)
# # luigi = Player("Luigi", "Super Blooper", mario)

# # print(get_rank(luigi))
# # print(get_rank(peach))
# # print(get_rank(mario))


# class Villager:
#     def __init__(self, name, species, catchphrase):
#         self.name = name
#         self.species = species
#         self.catchphrase = catchphrase
#         self.furniture = []

#     def greet_player(self, player_name):
#         return f"{self.name}: Hey there, {player_name}! How's it going, {self.catchphrase}!"

#     def add_item(self, item_name):
#         allowed = {"acoustic guitar", "ironwood kitchenette", "rattan armchair", "kotatsu", "cacao tree"}
#         if item_name in allowed:
#             self.furniture.append(item_name)


# alice = Villager("Alice", "Koala", "guvnor")
# print(alice.furniture)

# alice.add_item("acoustic guitar")
# print(alice.furniture)

# alice.add_item("cacao tree")
# print(alice.furniture)

# alice.add_item("nintendo switch")
# print(alice.furniture)


class Node:
    def __init__(self, fish_name, next=None):
        self.fish_name = fish_name
        self.next = next

# For testing
def print_linked_list(head):
    current = head
    while current:
        print(current.fish_name, end=" -> " if current.next else "\n")
        current = current.next

def catch_fish(head):
    if not head:
        print("Aw! Better luck next time!")
        return
    print(f"I caught a {head.fish_name}!")
    head = head.next # not clean way?

fish_list = Node("Carp", Node("Dace", Node("Cherry Salmon")))
empty_list = None

print_linked_list(fish_list)
print_linked_list(catch_fish(fish_list))
print(catch_fish(empty_list))


