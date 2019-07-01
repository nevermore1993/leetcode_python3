// 典型的动态规划问题，如果使用递归调用，十分的耗时
class Solution:
    def fib(self, N: int) -> int:
        if N == 0:
            return 0
        if N == 1:
            return 1
                 
        return self.fib(N-1) + self.fib(N-2)
        
// 使用dp方法，快几十倍
class Solution:
    def fib(self, N: int) -> int:
        if N == 0:
            return 0
        if N == 1:
            return 1
        dp = [0] * (N+1)
        dp[1] = 1
        for i in range(2,N+1):
            dp[i] = dp[i-1]+dp[i-2]
        return dp[N]
        
// 甚至不保存所有的子问题，只保存最近的两个子问题  
class Solution:
    def fib(self, N: int) -> int:
        a,b = 0,1
        for _ in range(N):
            a, b = b, a+b
        return a
