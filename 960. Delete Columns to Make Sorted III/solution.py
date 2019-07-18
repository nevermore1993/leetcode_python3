// dp[i]代表以第i列位结尾的最长升序子串的长度，注意，一定是要以第i列为结尾的。
// 那么在之前的0-(i-1)列中，如果第i列的每一行的值都比第j列的每一行的值要大，那么说明这一列可以接在第j列之后
// 则 dp[i] = max(dp[i], dp[j]+1)
// 如果有任何一行的值小于第j列的对应值，那么这一列就不能接在第j列前，则dp[i] = max(dp[i], 1)
// 但是其实dp[i]的最小值就是1，所以这个判断其实可以不要
// 每个dp[m]的初始值都是1
// 则最后的答案就是len(A[0]) - dp中最大的那个值

// 我开始想要将dp[i]设计为到这一列为止，能取到的最长子串，可以不包含这一列。但是这样的问题就是如果这一列不大于之前的某一列j，它也并不能
// 继承列j的长度，因为他们没有关系。如果继承了列j的长度，假设，之后的列m大于列i，那么根据我们的转换条件，dp[m] = dp[i] + 1
// 但是这个dp[i]是继承自dp[j]的，而我们并不能保证列m大于列j，所以就会出现问题。所以dp[i]的设计不能是这样的含义，而应该是包含列i的子串长度
class Solution:
    def minDeletionSize(self, A: List[str]) -> int:
        dp = [1] * len(A[0])
        for i in range(1, len(A[0])):
            for j in range(i-1,-1,-1):
                flag = True
                for row in A:
                    flag = flag & (row[i] >= row[j])
                    if not flag:
                        break
                if flag:
                    dp[i] = max(dp[i], dp[j] + 1)
        return len(A[0]) - max(dp)
