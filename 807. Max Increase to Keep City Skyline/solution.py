// 上下的轮廓线一样，左右的轮廓线一样  每个位置的最大值不能超过对应位置轮廓线的最小值，否则会改变轮廓线
// 所以每个位置的最大值为 min(left[i],top[j])

class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        top = []
        left = []
        result = 0
        for i in range(len(grid[0])):
            top.append(max([row[i] for row in grid]))
        for j in range(len(grid)):
            left.append(max(grid[j]))
        
        for i in range(len(grid[0])):
            for j in range(len(grid)):
                result += (min(left[i], top[j]) - grid[i][j])
        return result
