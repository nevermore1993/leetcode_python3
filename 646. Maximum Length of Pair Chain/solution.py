// dp[i]代表包含pairs[i]能达到的最大长度
// 如果pairs是无序的，那么不能使用dp算法，因为后面可能会出现可以插在之前序列的pair，所以会影响之前的dp[j]
// 所以先将pairs按照pair[0]的升序排序，然后再使用dp算法
class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs = sorted(pairs, key=lambda x:x[0])
        dp = [1] * len(pairs)
        for i in range(1, len(pairs)):
            for j in range(i):
                if pairs[i][0] > pairs[j][1]:
                    dp[i] = max(dp[i], dp[j]+1)
        return max(dp)
        

// 将pairs按照pair[1]的升序排序，那么每个pair的结束位置越小，则这个链肯定越长，贪心算法。
class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key=lambda x: x[1])
        cur, ans = float('-inf'), 0
        for x, y in pairs:
            if cur < x:
                cur = y
                ans += 1
        return ans
