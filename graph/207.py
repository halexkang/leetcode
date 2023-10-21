# Idea:
# - since prereq has to come before main course, it is a DAG
# - problem can be reduced to -> detecting cycles
# - we can use DFS / Topological ordering to defect cycles

# Topological sorting:
# - aligning all nodes in a line in a way that all edges point to the right
# - only DAGs have topological sorting, because if cycle exists,
#   at least one edge will point in the other direction
# - useful when one thing needs to happen before another, ex: prereq, dependency, etc

# Kahn's algorithm:
# - remove nodes without dependency
# - after removing nodes, new nodes without dependency will appear
# - if not all nodes can be removed, cycle exists
# - indegree: number of dependencies
# Pseudocode:
# find all node's indegree
# add all nodes with 0 indegree to the queue
# pop a node from the queue, and reduce the indegree of node's children by 1
# repeat until queue is empty, if unexplored node exists, cycle exists

# DFS:
# - if a decendent is already being explored, there is a back edge, which means cycle exists
# - use 3 states to denote, not visited, visiting, and visited
# - each node explores it's descendants.
# - if any descendant is visited, don't explore again
# - if any descendant is being visited, cycle exists
# - update current node to visited after exploring all descendants
# - check if cycle exists starting every node.

# Topological sorting
from collections import deque

def canFinish_TS(numCourses, prerequisites):
    # create adj list
    adj = [[] for _ in range(numCourses)]
    for m, pre in prerequisites:
        adj[pre].append(m)
    # find in degrees
    in_degrees = [0] * numCourses
    for course, prereq in prerequisites:
        in_degrees[course] += 1
    queue = deque()
    # add all nodes with in degree of 0
    for i in range(numCourses):
        if in_degrees[i] == 0:
            queue.append(i)
    cnt = 0 # success cond -> num_visited == numCourses
    res = []
    
    while queue:
        i = queue.popleft()
        res.append(i)
        cnt += 1
        
        for des in adj[i]:
            in_degrees[des] -= 1
            if in_degrees[des] == 0:
                queue.append(des)
    if cnt != numCourses: # terminated before exploring all nodes, cycle exists
        return False
    return True

# DFS with 3 colors
def canFinish_DFS(numCourses, prerequisites):
    # create adj list
    adj = [[] for _ in range(numCourses)]
    for m, pre in prerequisites:
        adj[pre].append(m)
    state = [-1] * numCourses # -1 -> not visited

    # if one of descendent is being visited, cycle exists
    def cycle(i):
        if state[i] == 1: # 1 -> visited, pass
            return False
        if state[i] == 0: # 0 -> visiting, means backedge
            return True
        state[i] = 0 # set to visiting
        for des in adj[i]: # explore neighbors
            if cycle(des): # if at least one of them has a cycle, cycle exists
                return True
        state[i] = 1 # set to visited after exploring all descendent
    
    for c in range(numCourses): # check for every course
        if cycle(c):
            return False
    return True

# Topological sort using kahn's algorithm