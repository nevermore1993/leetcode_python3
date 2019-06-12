// 依次取出A,B中的元素，判断交集，重点是判断下一个是取A中的元素还是B中的元素，那么就要判断现在取出的元素是A的大还是B的大。
// 我这里判断了所有的情况，来决定下一个是取A的还是B的。首先判断当前两个元素没有交集的情况，然后判断A大还是B大的情况
class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        i, j = 0, 0
        result = []
        while i < len(A) and j < len(B):
            ta = A[i]
            tb = B[j]
            if ta[0] > tb[1]:
                j += 1
                continue
            elif tb[0] > ta[1]:
                i += 1
                continue
            else:
                if ta[1] < tb[1]:
                    i += 1
                    result.append([max(ta[0], tb[0]), ta[1]])
                    continue
                elif tb[1] < ta[1]:
                    j += 1
                    result.append([max(ta[0], tb[0]), tb[1]])
                    continue
                else:
                    i += 1
                    j += 1
                    result.append([max(ta[0], tb[0]), ta[1]])
                    continue
        return result
        
        

// 首先判断是否有交集。然后根据两个右边界，判断下一个取A的还是B的。如果右边界相等，下一个取哪一个都可以，因为下一次会没有交集，只不过浪费了
// 一次循环。
class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        ans = []
        i = j = 0

        while i < len(A) and j < len(B):
            # Let's check if A[i] intersects B[j].
            # lo - the startpoint of the intersection
            # hi - the endpoint of the intersection
            lo = max(A[i][0], B[j][0])
            hi = min(A[i][-1], B[j][-1])
            if lo <= hi:
                ans.append(Interval(lo, hi))

            # Remove the interval with the smallest endpoint
            if A[i][-1] < B[j][-1]:
                i += 1
            else:
                j += 1

        return ans

