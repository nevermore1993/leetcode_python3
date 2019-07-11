// 与我设计的dp相同，dp[x]代表day[x-1]这一天能够取到的最小值
// 问题是如何利用dp[x-1]来得到dp[x].事实上应该使用之前的若干个dp[x]来决定dp[x]。
// 我一开始思考的是，dp[x]代表以这一天作为一张票的周期的结尾。也就是说接下来的一天不能被包含在dp[x]这一天的票之内。
// 那么我们往前找，先是1天的，那么就是dp[x] = dp[x-1] + cost[0].
// 然后是7天的，也就是从x这一天为结尾，之前七天内被一张票覆盖。那么假设最后一个不包含在这7天之内的为m天，那么dp[x] = dp[m] + cost[1]
// 同理30天的，假设之前30天之外的为n天，那么dp[x] = dp[n] + cost[2]
// 比较这三个大小，选择最小的。但是这个方法有个麻烦的地方，就是要找到7天和30天所能覆盖的范围，因为天数并不是连续的。

// 而这个解法就是对之前每一天都进行遍历，7天内的都是加cost[1]，30天内的都是加cost[2]。
class Solution(object):
    def mincostTickets(self, days, costs):
		# Prevent the assumption cost[0] < cost[1] < cost[2] not holds (e.g. [15, 2, 7])
        for i in range(len(costs)):
            costs[i] = min(costs[i:])
		# Note that dp[i] represents the min cost of days[i-1]
        dp = [float('inf')] * (len(days)+1)
        dp[0] = 0
        for i in range(len(days)):
            for j in range(i, -1, -1):
                gap = days[i] - days[j] + 1
				# we only need to consider the gap within 30 days window
                if gap > 30:
                    break
				# in this case, i=j
                elif gap == 1:
                    dp[i+1] = min(dp[i+1], dp[j] + costs[0])
                elif gap <= 7:
                    dp[i+1] = min(dp[i+1], dp[j] + costs[1])
                else:
                    dp[i+1] = min(dp[i+1], dp[j] + costs[2])
        return dp[-1]
