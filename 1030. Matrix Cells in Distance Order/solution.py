// 从r0,c0开始遍历，距离r0,c0长度为1的点为其四个方向上的邻居(在矩阵内的)。然后距离这些邻居1的点为距离r0,c0距离2的点，以此类推
// 对整个矩阵进行遍历。要先对所有距离相同的点遍历完成后，再遍历下一个距离的点。并且在遍历时，要注意对已经遍历过的点进行记录。
// 有可能某个点到另外两个点的距离相同，所以要防止出现重复的情况
// 创建二维数组时，如果使用[[0]*C]*R这样的形式，所有的行的引用其实都指向第一行，所以对某一行的某个值进行修改，也会影响其他行相同位置的值。
// 应使用下面所示的声明方法
class Solution:
    def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
        flag = [[0] * C for i in range(R)]
        flag[r0][c0] = 1
        res = []
        def helper(l):
            if len(l) == 0:
                return
            nextL = []
            for cell in l:
                res.append(cell)
                r, c = cell[0], cell[1]
                if r+1 < R and flag[r+1][c] == 0:
                    nextL.append([r+1,c])
                    flag[r+1][c] = 1
                if r-1 > -1 and flag[r-1][c] == 0:
                    nextL.append([r-1,c])
                    flag[r-1][c] = 1
                if c+1 < C and flag[r][c+1] == 0:
                    nextL.append([r,c+1])
                    flag[r][c+1] = 1
                if c-1 > -1 and flag[r][c-1] == 0:
                    nextL.append([r,c-1])
                    flag[r][c-1] = 1
            helper(nextL)
        helper([[r0,c0]])
        return res
        
        
// 按顺序遍历所有的点，将距离相同的点放在一个字典的key下面，然后按照顺序加入到结果中      
from collections import defaultdict
class Solution:
    def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
        i = 0
        dist = defaultdict(list)
        
        while i < R:
            j = 0
            while j < C:
                d = abs(r0 - i) + abs(c0 - j)
                dist[d].append((i,j))
                j += 1
            i += 1
            
        i = 0
        res = []
        while i <= (R + C):
            if i in dist:
                res += dist[i]
            i += 1
                
        return res
