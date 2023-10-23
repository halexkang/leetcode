# variant of DFS
# 1. go left
# 2. go right
# 3. visit node

from treenode import test_tree
root = test_tree()

def postorder(root):
    def helper(root, res):
        if root:
            helper(root.left, res)
            helper(root.right, res)
            if root.val:
                res.append(root.val)
    res = []
    helper(root, res)
    return res

print(postorder(root))