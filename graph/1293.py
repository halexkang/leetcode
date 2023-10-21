# https://leetcode.com/problems/shortest-path-in-a-grid-with-obstacles-elimination/
# 1293. Shortest Path in a Grid with Obstacles Elimination

# Idea:
# - finding shortest path -> use BFS
# - if there are multiple paths to the same cell, use path with higher k value, 
#   and to do that, k must be tracked.
# - pass steps so that it can be returned

# Stop exploring condition:
# - if out of bounds, don't explore
# - if not enough k, don't explore
# - if a previous path is better (has higher k), don't explore

# Time Complexity:
# - need to traverse the grid (M*N)
# - can explore the same cell up to k times (k)
# Total: O(M*N*k)

# Space Complexity:
# - need to store all cells (M*N)
# - lengh of queue is at worst holding all cells (M*N)
# Total: O(M*N)

from collections import deque

def shortestPath(grid, k):
    num_rows = len(grid)
    num_cols = len(grid[0])

    visited = {}
    queue = deque()
    root = (0, 0, 0, k)
    queue.append(root)
    while len(queue):
        node = queue.popleft()
        i, j, steps, k_i = node
        if i == num_rows-1 and j == num_cols-1: # success
            return steps
        if i < 0 or j < 0 or i >= num_rows or j >= num_cols: # out of bounds
            continue
        if (i, j) in visited and k_i <= visited[(i,j)]: # not a better path
            continue
        visited[(i,j)] = k_i # add to visited
        if grid[i][j] == 1: # if obstacle, use k
            k_i -= 1
            if k_i < 0: # if don't have k, can't continue path
                continue
        
        steps += 1
        queue.append((i-1, j, steps, k_i))
        queue.append((i+1, j, steps, k_i))
        queue.append((i, j-1, steps, k_i))
        queue.append((i, j+1, steps, k_i))
    return -1