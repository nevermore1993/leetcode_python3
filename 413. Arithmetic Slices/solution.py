// 找出所有最大的等差数列子串。且不同的等差数列不会重叠，因为差不同。然后根据每个等差数列的长度，计算其中等差字串的数目
// 假设等差数列长度为n，则其中等差字串的数目为 (n-2)+(n-3)+...+2+1 = (n-1)(n-2)/2
// l为当前等差数列的长度。当下一个元素满足当前等差数列的条件时，l加一。否则l变为2，即当前元素和下一个元素组成的数列。
// 当l变为2的时候，如果之前的数列长度大于3，则说明是一个有效的最大等差数列，可以加入到结果中。
class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        l = 0
        diff = 0
        res = 0
        for i in range(len(A)-1):
            if l == 0:
                diff = A[i+1] - A[i]
                l += 2
            else:
                if diff == A[i+1] - A[i]:
                    l += 1
                else:
                    if l >= 3:
                        res += (l-1)*(l-2)//2
                    l = 2
                    diff = A[i+1] - A[i]
        if l >= 3:
            res += (l-1)*(l-2)//2
        return res
        
        
        

// dp算法。dp[i]表示如果(i+2)是也是当前等差数列的一员，那么这次拓展会为之前的这个等差数列增加多少子等差数列。
// 而dp[i-1]这次拓展所增加的所有子数列都会因为这次拓展而拓展，所以dp[i]这次拓展所添加的子数列为dp[i-1]+1
// 这个1代表新出现的(i,i+1,i+2)。那么总结果就多了dp[i]个子数列
class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        memo = [0] * len(A)
        num = 0
        for i in range(0, len(A)-2):
            if A[i] - A[i+1] == A[i+1] - A[i+2]:
                memo[i] = memo[i-1] + 1
                num += memo[i]
        return num

