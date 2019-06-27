// 只有当上和下，左和右的步数一样时，才能回到原点

class Solution:
    def judgeCircle(self, moves: str) -> bool:
        dic = {"U":0,"D":0,"L":0,"R":0}
        for c in moves:
            dic[c] += 1
        if dic["U"] == dic["D"] and dic["R"] == dic["L"]:
            return True
        else:
            return False



//也可以使用内置的list.count(a)来统计每种动作的数目，从结果上看，内置的函数要快的多
class Solution:
    def judgeCircle(self, moves: str) -> bool:
        return moves.count('U') == moves.count('D') and moves.count('L') == moves.count('R')
