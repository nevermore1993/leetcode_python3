// 最简洁的方法，但是不是最快的，因为至少进行了两次遍历
class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        return A.index(max(A))
        
        
        
// 类似二分法，因为数组是符合递增然后递减的规律的，通过检查中心位置的增减性，就可以知道顶峰坐落于哪一个半区       
class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        lo = 0
        hi = len(A)-1
        
        while (True):
            mid = (lo+hi)//2
            if A[mid+1] < A[mid] and A[mid] > A[mid-1]:
                return mid
            elif A[mid+1] > A[mid]:
                lo = mid
            else:
                hi = mid
