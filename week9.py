from collections import deque 

# Tree Node class
class TreeNode:
  def __init__(self, value, key=None, left=None, right=None):
      self.key = key
      self.val = value
      self.left = left
      self.right = right

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

def merge_orders(order1, order2):
    if not order1:
        return order2
    if not order2:
        return order1
    
    s=TreeNode(order1.val+order2.val)

    s.left=merge_orders(order1.left,order2.left)
    s.right=merge_orders(order1.right,order2.right)

    return s

cookies1 = [1, 3, 2, 5]
cookies2 = [2, 1, 3, None, 4, None, 7]
order1 = build_tree(cookies1)
order2 = build_tree(cookies2)

# Using print_tree() function included at top of page
print_tree(merge_orders(order1, order2))

class Puff():
     def __init__(self, flavor, left=None, right=None):
        self.val = flavor
        self.left = left
        self.right = right

def print_design(design):
    if not design:
        return []

    queue = deque([design])
    flavors = []

    while queue:
        current = queue.popleft()
        flavors.append(current.val)

        if current.left:
            queue.append(current.left)
        
        if current.right:
            queue.append(current.right)

    print(flavors)

croquembouche = Puff("Vanilla", 
                    Puff("Chocolate", Puff("Vanilla"), Puff("Matcha")), 
                    Puff("Strawberry"))
print_design(croquembouche)

    

def max_tiers(cake):
    # cake is not return 0
    if not cake:
        return 0
    queue = deque([cake])
    count = 0

    while queue:
        current = queue.popleft()
        # do something to ++count
        # if we are the last element len(queue) then we can increment
        if len(queue) == 1:
            count += 1

        if current.left:
            queue.append(current.left)
        
        if current.right:
            queue.append(current.right)

    
    return count + 1
    
cake_sections = ["Chocolate", "Vanilla", "Strawberry", None, None, "Chocolate", "Coffee", "Matcha", "pop"]
cake = build_tree(cake_sections)

print(max_tiers(cake))

def max_tiers(cake):
    if not cake:
        return 0
    left_depth=max_tiers(cake.left)
    right_depth=max_tiers(cake.right)

    return 1+max(left_depth,right_depth)

cake_sections = ["Chocolate", "Vanilla", "Strawberry", None, None, "Chocolate", "Coffee"]
cake = build_tree(cake_sections)

print(max_tiers(cake))