
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


# Write a function to return the zigzag level order traversal of a binary tree. In a zigzag traversal, the nodes are visited level by level, but the direction alternates between left-to-right and right-to-left for each level.
# Input: root = [3, 9, 20, null, null, 15, 7]
# Output: [[3], [20, 9], [15, 7]]
# Explanation:
# Level 1: [3] (left-to-right)
# Level 2: [20, 9] (right-to-left)
# Level 3: [15, 7] (left-to-right)


def zig_zag(root):
    # use queue to level, but in order to alternate have a bool (rightLeft = true)
        # if its true - > go reverse (right child to left) put in stack then iterate backwards
        #               make rightLeft = false collect children
                        # append to return
        # else (rightLeft = false) -> normal pop, append to return
    # return list of zig zags

    if not root:
        return []
    
    queue = deque([root])
    zig_zagsList = []
    leftRight = True # flip this at each iter

    while queue:
        if leftRight is False:
            level_size = len(queue)
            to_add = []
            temp = []

            for _ in range(level_size):
                x = queue.popleft()
                temp.append(x.val)
                if x.left:
                    queue.append(x.left)
                if x.right:
                    queue.append(x.right)

            to_add.append(temp[::-1])
            zig_zagsList.append(to_add)
            leftRight = True
        else:
            level_size = len(queue)
            to_add = []

            for _ in range(level_size):
                curr = queue.popleft()
                to_add.append(curr.val)

                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            
            zig_zagsList.append(to_add)
            leftRight = False

    return zig_zagsList

        

root = [3, 9, 20, 10, 30, 15, 7]
to_test = build_tree(root)
print(zig_zag(to_test))