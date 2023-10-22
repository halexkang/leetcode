# https://leetcode.com/problems/number-of-islands/description/
# 200. Number of Islands

# Idea:
# - explore connected components, set it to visited.
# - if a connected component is found, cnt += 1
# - traverse until all nodes are explored -> -1
def numIslands(grid):
    def dfs(i, j):
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]):
            return
        if grid[i][j] == '0' or grid[i][j] == '-1':
            return
        grid[i][j] = '-1'
        dfs(i+1, j)
        dfs(i-1, j)
        dfs(i, j+1)
        dfs(i, j-1)
    cnt = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '1':
                cnt += 1
                dfs(i,j)
    return cnt