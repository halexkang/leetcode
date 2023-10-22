# https://leetcode.com/problems/flood-fill/submissions/
# 733. Flood Fill

# Idea:
# - traverse through the graph where value == original_value
# - both BFS and DFS will work

from collections import deque

def floodFill_BFS(image, sr, sc, color):
    grid, i, j, val = image, sr, sc, color # for simplicity
    queue = deque()   
    queue.append((i, j))
    visited = set()
    ori = grid[i][j]
    while len(queue):
        i, j = queue.popleft() 
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]):
            continue
        if (i, j) in visited:
            continue
        if grid[i][j] != ori:
            continue
        grid[i][j] = val
        visited.add((i, j))
        queue.append((i+1, j))
        queue.append((i-1, j))
        queue.append((i, j+1))
        queue.append((i, j-1))
    return grid


def floodFill_DFS(image, sr, sc, color):
    grid, i, j, val = image, sr, sc, color # for simplicity
    ori_val = grid[i][j]
    visited = set()
    def dfs(i, j):
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]):
            return
        if grid[i][j] != ori_val:
            return
        if (i, j) in visited:
            return
        visited.add((i, j))
        grid[i][j] = val
        dfs(i+1, j)
        dfs(i-1, j)
        dfs(i, j+1)
        dfs(i, j-1)
    dfs(i, j)
    return grid