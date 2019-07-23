// 因为每次都需要取出最大的两个数，所以很自然的想到使用大顶堆，而heapq只能实现小顶堆，所以将原数组的相反数存入小顶堆中实现大顶堆
// 然后模拟题目的要求，一步一步进行就可以了
// 也可以每次都进行排序，但是明显这样效率很低

import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        pq = [-x for x in stones]
        heapq.heapify(pq)
        for i in range(len(stones) - 1):
            x, y = -heapq.heappop(pq), -heapq.heappop(pq)
            heapq.heappush(pq, -abs(x - y))
        return -pq[0]
