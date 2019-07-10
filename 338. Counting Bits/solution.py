// result[i*2] = result[i] 因为 i*2 = i 右移一位, 1的数目没有变
// result[i*2+1] = result[i] + 1 因为 i*2+1 = i 右移一位再加1, 1的数目加1
// 只用考虑dp[0]，其余的都可以用dp[0]得到。
class Solution:
    def countBits(self, num: int) -> List[int]:
        dp = [0] * (num+1)
        dp[0] = 0
        if num < 1:
            return dp
        for i in range(1,num+1):
            if i%2 == 0:
                dp[i] = dp[i//2]
            else:
                dp[i] = dp[i//2] + 1
        return dp
        
// 假设 2^n < x < 2^(n+1), 则x = 2^n + (x - 2^n),所以x的1的个数等于2^n的1的个数+(x-2^n)的1的个数      
class Solution:
    def countBits(self, num: int) -> List[int]:
        result = [0] * (num+1)
        bit = 0
        for i in range(1,num+1):
            if 2**bit == i:
                result[i] = 1
                bit += 1
            else:
                result[i] = result[2**(bit-1)] + result[i - 2**(bit-1)]
        return result                

    
// 如果没有进位，i&(i-1)得到的就是(i-1)，那么就只多了一个1。如果有进位，进位的部分变为了0，进的位多了一个1，
// 假设进位的部分长度为x，也就是少了x个1，多了1个1。i&(i-1)就会将x+1位都变为0，再加上进位的一个1。
class Solution:
    def countBits(self, num: int) -> List[int]:
        res = [0]*(num+1)
        for i in range(1,num+1):
            res[i] = res[i&(i-1)] + 1
        return res
