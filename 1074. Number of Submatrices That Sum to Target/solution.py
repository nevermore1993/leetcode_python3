// 遍历所有的子矩阵，以子矩阵的列数来区分。(从第一列开始，1列，2列，3列的；从第二列开始，1列，2列，3列...)
// 先将每一行的元素累加，那么row[j]-row[i]的值就是这一行从i-j这个区间的元素的和。
// 对于某一类确定列数的子矩阵，逐行累加，得到这种列数的不同行数的子矩阵的和。但是只计算了1行，2行，3行的子矩阵，不同行数应该有不同的子矩阵。
// 所以我们将每次累加得到的子矩阵保存在字典c中，然后用cur-target来判断，子矩阵中是否有满足条件的。
// 不需要计算所有的情况，只需要计算每层累加的，所有的情况都可以通过不同层之间的减法得到。就像是开始将每行的元素累加，通过row[j]-row[i]可以得到
// 这一行任意块组合的和

class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        m, n = len(matrix), len(matrix[0])
        for row in matrix:
            for i in range(n - 1):
                row[i + 1] += row[i]
        res = 0
        for i in range(n):
            for j in range(i, n):
                c = collections.Counter({0: 1})
                cur = 0
                for k in range(m):
                    cur += matrix[k][j] - (matrix[k][i - 1] if i > 0 else 0)
                    res += c[cur - target]
                    c[cur] += 1
        return res
