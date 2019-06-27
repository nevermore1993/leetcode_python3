// 先排序再计算平方    先平方再排序 
class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        A.sort(key = lambda x: abs(x))
        for i in range(len(A)):
            A[i] = A[i] ** 2
        return A
        
// 最简洁的方式
class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        return sorted(x*x for x in A)
