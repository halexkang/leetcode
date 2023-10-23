# variation of BFS
# 1. create queue
# 2. visit node
# 3. add children to queue

from treenode import test_tree
root = test_tree()

def levelorder(root):
    res = []
    if root:
        queue = [root]
        while queue:
            node = queue.pop(0)
            if node.val:
                res.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    return res

print(levelorder(root))