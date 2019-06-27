// 利用类似快排的思路，start和end从头尾开始遍历，交换奇偶。与快排不同的是，这里没有一个标准值来决定交换哪两个，而是由奇偶决定的
// 所以与快排有区别

class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        start = 0
        end = len(A) - 1
        while start < end:
            while start < end and A[start] % 2 == 0:
                start += 1
            while start < end and A[end] % 2 != 0:
                end -= 1
            temp = A[start]
            A[start] = A[end]
            A[end] = temp
        return A
        


// 遍历数组，将奇偶插入到新数组的头或者尾，因为没有交换操作，所以比上面的方法要快，但是占用额外的空间，不是in-place sort
class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        res = [0] * len(A)
        start = 0
        end = len(A) - 1
        for a in A:
            if a % 2 == 0:
                res[start] = a
                start += 1
            else:
                res[end] = a
                end -= 1
        return res
        
// 利用内置函数排序，慢    
class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        A.sort(key = lambda x:x&1)
        return A
