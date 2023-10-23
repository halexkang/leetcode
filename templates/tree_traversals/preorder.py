# variant of DFS
# 1. visit node
# 2. go left
# 4. go right

from treenode import test_tree
root = test_tree()

def preorder(root):
    def helper(root, res):
        if root:
            if root.val:
                res.append(root.val)
            helper(root.left, res)
            helper(root.right, res)
    res = []
    helper(root, res)
    return res

print(preorder(root))