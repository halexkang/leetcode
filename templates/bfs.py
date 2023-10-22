from collections import deque

def bfs(root):
    visited = set()
    queue = deque()
    queue.append(root)
    visited.add(root)
    while len(queue):
        node = queue.popleft()
        do_something(node)
        for node in get_neighbors(): 
            if node not in visited: 
                queue.append(node) 
                visited.append(node) 


# helpers
def do_something(node):
        pass

def get_neighbors(node):
    pass
        


