// 提取出虚部和实部，分别计算结果
class Solution:
    def string2array(self, s):
        res = []
        temp = 0
        posorneg = 1
        for i in range(len(s)):
            if s[i] == 'i':
                break
            if s[i] == '-':
                posorneg = -1
                if i != 0:
                    temp = 0
            elif s[i] == '+':
                posorneg = 1
                if i != 0:
                    temp = 0
            else:
                temp = temp * 10 + int(s[i])
                if not s[i+1].isdigit():
                    res.append(temp * posorneg)
        return res
                
    def complexNumberMultiply(self, a: str, b: str) -> str:
        a1 = self.string2array(a)
        b1 = self.string2array(b)
        num = a1[0] * b1[0] - a1[1] * b1[1]
        fac = a1[0] * b1[1] + a1[1] * b1[0]
        res = str(num) + '+' + str(fac) + 'i'
        return res
        

// 虚部和实部是通过'+'分隔的
class Solution:
    def complexNumberMultiply(self, a: str, b: str) -> str:
        real_a, imag_a = [int(x) for x in a[:-1].split('+')]
        real_b, imag_b = [int(x) for x in b[:-1].split('+')]
        real_c = real_a*real_b - imag_a*imag_b
        imag_c = real_a*imag_b + imag_a*real_b
        return f'{real_c}+{imag_c}i'

