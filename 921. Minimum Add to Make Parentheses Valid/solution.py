// 统计'('的数量，当有新的'('出现时，加一，当已经存在'('时，出现')'的话减一，如果没有可用的'('存在，出现了')'，
//则给'）'的数目加一，最后是两个的和。因为能在任意地方插入'()'，所以只用统计他们的数量。但是由于可能存在')('的情况，
//所以不能简单的抵消，要根据出现的先后次序决定是否能够抵消。
class Solution:
    def minAddToMakeValid(self, S: str) -> int:
        l = 0
        r = 0
        for char in S:
            if char == '(':
                l += 1
            else:
                if l > 0:
                    l -= 1
                else:
                    r += 1
        return l + r
