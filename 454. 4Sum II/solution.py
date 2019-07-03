// 简单的循环，三层循环，其实在count里应该也有一个循环，应该是四层循环，而且最后注意要统计D中所有满足条件的元素数量
class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        res = 0
        for i in A:
            for j in B:
                for z in C:
                    res += D.count(-(i+j+z))
        return res

// 将四层循环变为两个二层循环，也就是将计算量从n^4变为2*n^2. 第一个二层循环统计所有A,B的可能的和的数量。第二个二层循环统计C,D中符合条件
// 的和是否存在，对应的A,B的和的数量就是答案。
class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        ans = 0
        sum_ab = {}
        for a in A:
            for b in B:
                anb = a+b
                if anb in sum_ab:
                    sum_ab[anb] += 1
                else:
                    sum_ab[anb] = 1
        for c in C:
            for d in D:
                if -c-d in sum_ab:
                    ans += sum_ab[-c-d]      
        return ans
