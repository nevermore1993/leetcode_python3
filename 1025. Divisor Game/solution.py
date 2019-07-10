// dp算法。从1开始，N=1时，是False。N=2时，是True。dp[m]代表N=m时，先手的人是否能赢。
// 判断dp[N]的真假。从N开始，只经过一次操作，得到N-x，在所有的N-x的可能性中只要有
// dp[N-x]=False存在，就说明N为True。因为经过一次操作后，相当于先手的人变为Bob，而他起手的值为N-x。当有N-x为False时，就说明只要我们
// 经过一次操作，使得N变为N-x,那么Bob就会输，也就是我们会赢。
// 而偶数的N-x可以是奇数，也可以是偶数。而奇数的N-x只能是偶数。推断得到，所有偶数的都能赢。而所有奇数的都会输(因为奇数的下一步是偶数，为True
// 即后手的人会赢)
class Solution:
    def divisorGame(self, N: int) -> bool:
        if N%2 == 0:
            return True
        else:
            return False
