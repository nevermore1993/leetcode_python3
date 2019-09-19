// 设计dp代表的东西，找到转换关系，基础情况。时刻记得dp所代表的意义。
// dp[i]表示books[:i]放入书架的最小高度，且保证books[i-1]是最后一层的最后一本，之后再也放不下别的书，或者最后一层的唯一一本
// 而dp[i]与之前的dp[]的关系。
// 1.先是将books[i-1]单独放在一层的情况，dp[i]=dp[i-1]+books[i-1][1]
// 2.将之前若干本能够放在一层的books放在新的一层，假设之前3本书能够放在一层，那么dp[i]=dp[i-3]+max(books[i-3:i-1][1])
// 还要考虑只放两本的情况....
// 其实只有一种情况，dp[i]代表之前i-1本书的最佳摆放高度。我们的目的就是如何用新书和之前的书构建最后一层。这里有几种可能性
// 新书自己是一层/新书和之前若干本书组合成最后一层，判断这几种方法的最小高度。要注意，如果我们取了之前3本书，一定要在之前的
// i-3本书的基础上组成新的一层。
class Solution:
    def minHeightShelves(self, books: List[List[int]], shelf_width: int) -> int:
        n = len(books)
        dp = [float('inf') for _ in range(n + 1)]
        dp[0] = 0
        for i in range(1, n + 1):
            max_width = shelf_width
            max_height = 0
            j = i - 1
            while j >= 0 and max_width - books[j][0] >= 0:
                max_width -= books[j][0]
                max_height = max(max_height, books[j][1])
                dp[i] = min(dp[i], dp[j] + max_height)
                j -= 1
        return dp[n]
