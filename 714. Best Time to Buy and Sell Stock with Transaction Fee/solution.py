// 在位置i，有两种情况，我们持有股票/不持有股票
// 持有股票的情况，是我们在i-1就持有股票，但是在i什么都没干，则hold[i] = hold[i-1]
// 或者是我们在i-1不持有，在i买入，则hold[i] = notHold[i-1] - prices[i]
// 同理可得在i不持有股票的情况 notHold[i] = notHold[i-1] or hold[i-1] + prices[i] - fee

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        hold = [0] * len(prices)
        notHold = [0] * len(prices)
        res = 0
        hold[0] = -prices[0]
        for i in range(1, len(prices)):
            hold[i] = max(hold[i-1], notHold[i-1] - prices[i])
            notHold[i] = max(notHold[i-1], hold[i-1] + prices[i] - fee)
        return max(hold[-1], notHold[-1])
        
        
// 贪心算法
// 记录上一次买入时的价格，当我们遇上有盈利的卖出时，就卖出。但是如果这样可能会错过之后更大的盈利，所以在这次卖出的时候我们将
// 上次买入的价格更新为 p-fee，因为我们每多一笔交易，就多交一次fee。而我们进行了这笔交易之后，就相当于我们在之前的买入价格上多花费了fee
// 而上一次交易的盈利已经加入到res中，所以相当于买入价格更新为 p-fee。
// 也就是说我们这次卖出在当前是有盈利的，但是长远来看并不一定，可能确实是盈利，也可能是亏了，所以需要更新buy的值，并根据之后的价格判断
// 如果之后的买入价格很低，则这次卖出是合理的，如果不够低，则不合理，但是也不影响，因为我们已经更新了买入的价格。
// 假设最理想的卖出价格是p2,买入价格是p0,而我们实际的卖出价格是p1。那么最好的盈利是p2-p0-fee。而我们第一次卖出的盈利是p1-p0-fee，并
// 更新买入价格为p1-fee。那么我们第二次卖出的盈利是p2-(p1-fee)-fee=p2-p1，两次相加得p2-p0-fee,一样的。
class Solution:
    def maxProfit(self, prices, fee):
      """
      :type prices: List[int]
      :type fee: int
      :rtype: int
      """
      buy = prices[0]
      res = 0
      for p in prices:
          if buy > p: # current price is less than last buy
              buy = p # buy at p
          else:
              tmp = p - buy - fee
              if tmp > 0: # have profit
                  res += tmp
                  buy = p - fee 
      return res
