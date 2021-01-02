"""
HackerRank: Is This a Binary Search Tree?
https://www.hackerrank.com/challenges/is-binary-search-tree/problem

Node is defined as
class node:
  def __init__(self, data):
      self.data = data
      self.left = None
      self.right = None

"""
def check_binary_search_tree_(root):
    return validate(root, float('-inf'), float('inf'))

def validate(root, min_val, max_val):
    if not root:
        return True
    if root.data > min_val and root.data < max_val:
        return validate(root.left, min_val, root.data) and validate(root.right, root.data, max_val)
    else:
        return False