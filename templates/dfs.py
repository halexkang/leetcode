def dfs_binary(root):
    if not root:
        return
    do_something(root)
    dfs_binary(root.left)
    dfs_binary(root.right)


def dfs_graph(root, visited):
    if root in visited:
        return
    visited.add(root)
    do_something(root)
    for nei in get_neighbors(root):            
        dfs_graph(nei, visited)


# finds the max depth in a tree
def dfs_pass_up(root):
    if not root:
        return 0
    depth = 0
    for child in get_children(root):
        depth = max(depth, dfs_pass_up(child))
    return depth + 1


# print path of dfs
def dfs_pass_down(root, res):
    if not root:
        return
    res.append(root)
    dfs_pass_down(root.left, res)
    dfs_pass_down(root.right, res)


def backtrack(root):
    if not condition():
        return
    do_something(root)
    for child in get_children(root):
        backtrack(child)


# helpers
def do_something(root):
        pass

def get_children(root):
     pass


def get_neighbors(root):
    pass


def condition():
    pass