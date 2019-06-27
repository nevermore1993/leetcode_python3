// 将整数转换为二进制字符串，再比较。但是要注意两个字符串的长度可能不一样，所以要将两个字符串转换成同样的长度
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        b1 = bin(x)[2:]
        b2 = bin(y)[2:]
        if len(b1) < len(b2):
            b1 = '0'*abs(len(b1)-len(b2)) + b1
        else:
            b2 = '0'*abs(len(b1)-len(b2)) + b2
        res = 0
        for i in range(len(b1)):
            if b1[i] != b2[i]:
                res += 1
        return res
        
        
// 使用异或，然后与1，判断每一位是否为1        
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        distance = 0
        while x != 0 or y != 0:
            distance += (x ^ y) & 1
            x >>= 1
            y >>= 1
        return distance
