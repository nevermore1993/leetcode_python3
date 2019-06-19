// 没什么技巧，只不过是对python内置函数的应用。bin()将int转换为二进制字符串，如bin(3)='0b011'
// string.count(abegin=0,end=len(string))返回string中a出现的次数。类似的函数还有string.find(a),返回起始索引或-1
// string.index(a),返回起始索引或异常

class Solution:
    def queryString(self, S: str, N: int) -> bool:
        for i in range(1, N + 1):
            tmp = bin(i)[2:]
            if S.count(tmp) == 0:
                return False
        return True
