// 首先通过翻转行，将所有行的第一个元素变为1，因为第一位为1比剩下所有位都为1还要大。然后对剩下的每一列进行翻转，将尽可能多的元素变为1。
// 首先我翻转了第一列，然后统计剩下每一列的1的个数，如果超过半数就不需要翻转，否则需要翻转。而这里也可以不翻转，而直接用数量来计算和，因为我们
// 需要的就是1的个数，而不是其具体位置，因为固定位的1对总和的贡献是一样的。
class Solution:
    def flip(self, R: List[int]) -> List[int]:
        for i in range(len(R)):
            R[i] = 1 - R[i]
        return R[i]
    
    def count(self, C):
        count = 0
        for i in C:
            if i == 1:
                count += 1
        return count
    
    def matrixScore(self, A: List[List[int]]) -> int:
        res = 0
        for row in A:
            if row[0] == 0:
                self.flip(row)
            res += 2 ** (len(A[0]) - 1)
        print(A)
        for i in range(1,len(A[0])):
            R = [r[i] for r in A]
            count = self.count(R)
            if count < len(R) / 2:
                res += (len(R) - count) * 2 ** (len(A[0]) - i - 1)
            else:
                res += count * 2 ** (len(A[0]) - i - 1)
        return res
        
// 同样的思想，但是代码简洁多了。首先并不翻转第一列，直接计算第一列都是1的总和。然后对于剩下的列，当某元素与第一个元素相同时，说明在我们对
// 每一行进行翻转后，该位应该是一个1。比如，第一个元素是1，那么这里原来是什么，现在就是什么；而如果第一个元素是0，那么如果这里也是0，即跟
// 第一个元素相同，则翻转后为1，反之为0。所以如果这个元素和第一个元素相同，那么翻转过后就是1。通过这种方法统计每一列的1的个数，这样就不用
// 实际将第一列进行翻转，而可以在原矩阵中统计。
class Solution:
    def matrixScore(self, A: List[List[int]]) -> int:
        M, N = len(A), len(A[0])
        res = (1<<N-1)*M
        for j in range(1, N):
            cur = sum(A[i][j]==A[i][0] for i in range(M))
            res += max(cur, M-cur)*(1<<N-1-j)
        return res
