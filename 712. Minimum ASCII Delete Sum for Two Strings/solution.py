// dp[i][j]代表s1[:i]和s2[:j]要达到一致需要删除多少字符。
// 那么如果其中一个字符串是空的，则需要删除另一个字符串的所有字符才能一致，这是基本情况
// 那么如果s1[i] = s2[j]，则对于s1[:i]和s2[:j]达到一致所花费的和s1[:i-1],s2[:j-1]是一样的，即dp[i][j] = dp[i-1][j-1]
// 如果s1[i] != s2[j]，那么有两种情况，
// 1. s1[:i-1]和s2[:j]先达到一致，再删除s1[i]，即dp[i-1][j]+ord(s1[i])
// 2. s1[:i]和s2[:j-1]先达到一致，再删除s2[j]，即dp[i][j-1]+ord(s2[j])
// 比较这两种情况，选择较小的那个。
class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        """
        :type s1: str
        :type s2: str
        :rtype: int
        """
        l1, l2 = len(s1), len(s2)
        dp = [[0] * (l2 + 1) for _ in range(l1 + 1)]
        for i in range(1, l2+1):
            dp[0][i] = dp[0][i-1] + ord(s2[i-1])
        for i in range(1, l1+1):
            dp[i][0] = dp[i-1][0] + ord(s1[i-1])
            for j in range(1, l2+1):
                if s1[i-1] == s2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(ord(s1[i-1])+dp[i-1][j], ord(s2[j-1])+dp[i][j-1])
        return dp[l1][l2]
