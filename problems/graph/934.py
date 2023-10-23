# https://leetcode.com/problems/shortest-bridge/description/
# 934. Shortest Bridge

from collections import deque

def shortestBridge(grid):

    def invalid(i, j):
        return i < 0 or j < 0 or i >= n or j >= n

    def dfs(i, j): # use dfs to find all islands, and add all island nodes to bfs queue
        if invalid(i, j):
            return
        if grid[i][j] == 0:
            return
        if (i, j) in visited:
            return
        visited.add((i, j))
        for di, dj in offsets:
            dfs(i+di, j+dj)
            
    def bfs():
        queue = deque(visited)
        res = 0
        while len(queue):
            for _ in range(len(queue)): # flush all nodes in queue, see problem #102 (levelorder)
                i, j = queue.popleft()
                for di, dj in offsets:
                    ci, cj = i+di, j+dj
                    if invalid(ci, cj):
                        continue
                    if (ci, cj) in visited:
                        continue
                    if grid[ci][cj] == 1:
                        return res
                    queue.append((ci, cj))
                    visited.add((ci, cj))
            res += 1
        return -1

    offsets = [(1, 0), (-1, 0), (0, 1), (0, -1)] # used to find neighbors
    visited = set()
    n = len(grid)
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 1:
                dfs(i, j)
                return bfs()