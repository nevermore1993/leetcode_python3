// 先统计每个数字出现的次数，再排序
import collections
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict1 = collections.Counter(nums)
        dict2 = sorted(dict1.items(),key = lambda x:x[1],reverse=True)
        res = []
        for i in range(k):
            res.append(dict2[i][0])
        return res
        
        
// 先统计每个数字出现的次数，再放k个数字进入heapq中，在加入新的元素到heapq中时，会自动排序。如果新加入的元素比heapq中最小的要大
// 那么就替换最小的，如果比最小的还小，就跳过。这样不用排序，我们就得到了前k个最大的。
// 这里的h就是小顶堆，heapq.heappush(h, d[i])就是将元素d[i]添加到h中，heappop(h)就是弹出堆顶元素。
from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d, h = [(freq, num) for num, freq in Counter(nums).items()], []
        for i in range(k):
            heapq.heappush(h, d[i])
        for i in range(k, len(d)):
            if d[i][0] > h[0][0]:
                heapq.heappop(h)
                heapq.heappush(h, d[i])
        return [heapq.heappop(h)[1] for _ in range(k)][::-1]
