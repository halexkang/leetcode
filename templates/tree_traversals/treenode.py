class TreeNode:
    def __init__(self, val):
      self.left = None
      self.right = None
      self.val = val
   
def to_binary_tree(values, idx):
    if len(values) == 0:
        return None
    if idx > len(values)-1:
        return None
    root = TreeNode(values[idx])
    if 2*idx+1 < len(values):
        root.left = to_binary_tree(values, 2*idx+1)
    if 2*idx+2 < len(values):
        root.right = to_binary_tree(values, 2*idx+2)
    return root

def test_tree():
    values = [1, 2, 3, 4, 5, 6, 7, 8, None, None, None, 9, 10]
    root = to_binary_tree(values, 0)
    return root