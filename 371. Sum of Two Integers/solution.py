// 在不考虑进位的情况下，两数的和的每一位的结果与异或的结果相同。而每一位的进位情况与两个数的与运算的结果相同。
// 所以我们先计算没有进位时的和，再计算出进位，并左移一位。然后将进位与和相加。经过若干个循环，总能得到一个b=0，从而结束循环。
// 但是这个方法好像只能计算正数的和，不能计算整数的差。两个正整数的差就是一个正整数加上（另一个正整数取反加一）
// ~2+1 = -2.因为对原码取反加一是获得负数的补码的方法。当我们对正数a的符号位也取反时，就能得到-a。
class Solution:
    def getSum(self, a: int, b: int) -> int:
        if b == 0:
            return a
        s = a^b
        carry = (a&b)<<1
        return self.getSum(s,carry)
        
// 还可以使用python的内置sum(list)函数
class Solution:
    def getSum(self, a: int, b: int) -> int:
        return sum([a,b])
