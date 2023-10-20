# https://leetcode.com/problems/shortest-path-in-a-grid-with-obstacles-elimination/
# 1293. Shortest Path in a Grid with Obstacles Elimination

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