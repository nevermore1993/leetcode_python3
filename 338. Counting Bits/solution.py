// result[i*2] = result[i] 因为 i*2 = i 右移一位, 1的数目没有变
// result[i*2+1] = result[i] + 1 因为 i*2+1 = i 右移一位再加1, 1的数目加1
class Solution:
    def countBits(self, num: 'int') -> 'List[int]':
        if num % 2:
            result = [0]*(num+1)
        else:
            result = [0]*(num+2)
        result[1] = 1
        for i in range(1,num//2+1):
            result[i*2] = result[i]
            result[i*2+1] = result[i] + 1
        return result[:num+1]
        
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
        
