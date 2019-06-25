// 注意在使用for i in List 的时候，i并不是List中元素的引用，而是一个新的变量，对这个变量进行操作并不会影响原来数组中的值
class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        for l in range(len(A)):
            A[l] = A[l][-1::-1]
            
            for i in range(len(A[l])):
                print(A[l][i])
                A[l][i] = A[l][i] ^ 1
        return A
