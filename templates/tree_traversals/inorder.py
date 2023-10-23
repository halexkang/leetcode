# variant of DFS
# 1. go left
# 2. visit node
# 4. go right

from treenode import test_tree
root = test_tree()

def inorder(root):
    def helper(root, res):
        if root:
            helper(root.left, res)
            if root.val:
                res.append(root.val)
            helper(root.right, res)
    res = []
    helper(root, res)
    return res

print(inorder(root))