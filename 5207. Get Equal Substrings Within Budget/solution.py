// 使用滑动窗口，如果当前窗口的cost不大于max，则长度加一，如果大于cost，则将窗口整体右移。当我们找到第一个局部最长的子串的时候，
// 最后的结果肯定不会比这个短，所以我们滑动当前最优的子串，就能够覆盖所有的可能性。如果遇到可以拓展窗口的机会，就拓展

class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        res = 0
        start = 0
        end = 0
        tempCost = 0
        while end < len(s) and start <= end:
            # print(start,end,tempCost)
            # 新添加的cost
            newCost = abs(ord(s[end]) - ord(t[end]))
            tempCost += newCost
            # 如果不大于max，更新长度，拓展窗口
            if tempCost <= maxCost:
                res = max(res, end-start+1)
                end += 1
            # 否则整体右移窗口，并更新窗口cost
            else:
                tempCost -= abs(ord(s[start]) - ord(t[start]))
                start += 1
                end += 1
                
        return res
