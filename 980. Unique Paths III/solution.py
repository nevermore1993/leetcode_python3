// 最简单的方法，从1开始，遍历所有的路径，遇到-1就停，遇到2就检查是否遍历了所有的网格。对于已经走过的网格标记一下。但是因为所有
// 的路径都是用的是一个grid的引用，所以在一条路径结束后要将遍历过的点的标记去除。
class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        if not grid: return 0
        m,n = len(grid[0]),len(grid)
        for i in range(n):
            for j in range(m):
                if grid[i][j]==1: return self.helper(grid,i,j)
        return 0
    
    def helper(self,grid,row,col):
        m,n = len(grid[0]),len(grid)
        # 标记访问过的网格
        grid[row][col] = 3
        count = 0
        for mydir in [[0,1],[0,-1],[1,0],[-1,0]]:
            r,c = row+mydir[0],col+mydir[1]
            if 0<=r<n and 0<=c<m: 
                if grid[r][c]==0: count += self.helper(grid,r,c)
                elif grid[r][c]==2 and self.check(grid): count += 1
        # 去除访问过的网格的标记
        grid[row][col] = 0
        return count
    
    def check(self,grid):
        m,n = len(grid[0]),len(grid)
        for i in range(n):
            for j in range(m):
                if grid[i][j]==0: return False
        return True
