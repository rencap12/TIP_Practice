# Write your code here
from collections import deque 

# Tree Node class
class TreeNode:
  def __init__(self, value, key=None, left=None, right=None):
      self.key = key
      self.val = value
      self.left = left
      self.right = right

def print_tree(root):
    if not root:
        return "Empty"
    result = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    while result and result[-1] is None:
        result.pop()
    print(result)

def build_tree(values):
  if not values:
      return None

  def get_key_value(item):
      if isinstance(item, tuple):
          return item[0], item[1]
      else:
          return None, item

  key, value = get_key_value(values[0])
  root = TreeNode(value, key)
  queue = deque([root])
  index = 1

  while queue:
      node = queue.popleft()
      if index < len(values) and values[index] is not None:
          left_key, left_value = get_key_value(values[index])
          node.left = TreeNode(left_value, left_key)
          queue.append(node.left)
      index += 1
      if index < len(values) and values[index] is not None:
          right_key, right_value = get_key_value(values[index])
          node.right = TreeNode(right_value, right_key)
          queue.append(node.right)
      index += 1

  return root

#traverse through tree
#check node value, if its odd add one to counter
#once at the end of the tree exit def and return count      
def count_odd_splits(root):
    if not root:
        return 0
    if root.val % 2 != 0:
        return 1 + count_odd_splits(root.left) + count_odd_splits(root.right)
    
    return count_odd_splits(root.left) + count_odd_splits(root.right)
       

# from chat: 
#     count = 1 if root.val % 2 != 0 else 0
#     count += count_odd_splits(root.left)
#     count += count_odd_splits(root.right)
#     return count


values = [1, 3, 5, 6, 7, None, 12]
monstera = build_tree(values)

# print(count_odd_splits(monstera))
# print(count_odd_splits(None))


# Problem 2  
def find_flower(inventory, name):
    if not inventory:
        return False
    if inventory.val == name:
        return True
    if name < inventory.val:
        return find_flower(inventory.left, name)
    if name > inventory.val:
        return find_flower(inventory.right, name)

# using build_tree() function at top of page
values = ["Rose", "Lilac", "Tulip", "Daisy", "Lily", None, "Violet"]
garden = build_tree(values)

print(find_flower(garden, "Lilac"))  
print(find_flower(garden, "Sunflower")) 

# RAHAHAHAHHHHH

