// 直接对原数组排序，但是key使用lambda
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        points.sort(key=lambda x:x[0]*x[0]+x[1]*x[1])
        
        return points[0:K]
        
// 计算距离后，将距离和索引以字典的形式记录，对字典的值进行排序，再取出前K个键，就是索引        
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        dist = {}
        for i in range(len(points)):
            distance = points[i][0]**2 + points[i][1]**2
            dist.update({i:distance})
        sort = sorted(dist.items(),key=operator.itemgetter(1),reverse=False)
        res = []
        for i in range(K):
            res.append(points[sort[i][0]])
        return res
        
        
// 使用堆排序，每计算一个距离就加入到堆中，自动排序，计算完所有的距离后，最小的K个距离就计算出来了，直接返回就行了
// 这里是将距离和对应的(x,y)一起存在堆中，堆只对距离排序
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        heap = []
        
        for (x, y) in points:
            dist = -(x*x + y*y)
            if len(heap) == K:
                heapq.heappushpop(heap, (dist, x, y))
            else:
                heapq.heappush(heap, (dist, x, y))
        
        return [(x,y) for (dist,x, y) in heap]
