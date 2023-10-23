# https://leetcode.com/problems/binary-tree-level-order-traversal/description/
# 102. Binary Tree Level Order Traversal

# Idea:
# - BFS since we need to explore by level.
# - however, regular BFS will not group nodes in the same level
# - then, we can just handle push all nodes in a level to the queue, and handle it together.
from collections import deque

def levelOrder(root):
    if not root: return []
    res = []
    queue = deque()
    queue.append(root)
    while len(queue):
        tmp = []
        for _ in range(len(queue)):
            node = queue.popleft()
            if not node:
                continue
            tmp.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        if tmp:
            res.append(tmp)
    return res