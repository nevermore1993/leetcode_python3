// 规律是 1步右/下，2步左/上，3步右/下，4步左/下...... 只添加在矩阵中的位置，当所有的位置都被添加以后就可以结束循环了。
class Solution:
    def spiralMatrixIII(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
        i = 1
        res = [[r0,c0]]
        if len(res) == R*C:
            return res
        while i:
            for j in range(1, i+1):
                c0 += 1
                if r0 >= 0 and r0 < R and c0 >= 0 and c0 < C:
                    res.append([r0, c0])
                    if len(res) == R*C:
                        return res
            for j in range(1, i+1):
                r0 += 1
                if r0 >= 0 and r0 < R and c0 >= 0 and c0 < C:
                    res.append([r0, c0])
                    if len(res) == R*C:
                        return res
            for j in range(1, i+2):
                c0 -= 1
                if r0 >= 0 and r0 < R and c0 >= 0 and c0 < C:
                    res.append([r0, c0])
                    if len(res) == R*C:
                        return res
            for j in range(1, i+2):
                r0 -= 1
                if r0 >= 0 and r0 < R and c0 >= 0 and c0 < C:
                    res.append([r0, c0])
                    if len(res) == R*C:
                        return res
            i += 2
