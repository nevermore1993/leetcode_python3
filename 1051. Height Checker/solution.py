// 先排序，再比较不同
class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        sortA = sorted(heights)
        res = 0
        for i in range(len(sortA)):
            if sortA[i] != heights[i]:
                res += 1
        return res
