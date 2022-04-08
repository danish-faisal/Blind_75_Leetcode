# https://leetcode.com/problems/number-of-islands/

# Using BFS
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return
        
        rows, cols = len(grid), len(grid[0])
        islands=0
        visited=set()
        
        def bfs(row, col):
            visited.add((row,col))
            q=collections.deque()
            q.append((row,col))
            
            while q:
                row, col = q.popleft()
                dirs=[[0,-1],[1,0],[0,1],[-1,0]]
                for dr, dc in dirs:
                    r=row+dr
                    c=col+dc
                    if r in range(rows) and c in range(cols) and grid[r][c]=="1" and (r,c) not in visited:
                        visited.add((r,c))
                        q.append((r,c))
            
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]=="1" and (r,c) not in visited:
                    bfs(r,c)
                    islands+=1
        
        return islands