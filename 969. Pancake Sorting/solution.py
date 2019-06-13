// 首先将最大的元素翻转到第一个，再整体翻转，将最大的元素翻转到最后一个，然后对剩下的执行相同的操作，递归。
class Solution:
    def pancakeSort(self, A: List[int]) -> List[int]:
        if len(A) <= 1:
            return []
        
        if len(A) == 2:
            if A[0] == 1:
                return []
            else:
                return [2]
        
        //找到最大的元素
        index = 0
        for i in range(len(A)):
            if A[i] == len(A):
                index = i
                break
        //如果已经是最后一个了，就不用翻转
        if index == len(A) - 1:
            res = self.pancakeSort(A[:len(A) - 1])
        else:
        //如果不是最后一个，需要经过两步翻转将最大的元素放到最后。
            //第一次翻转之后的数组
            rev = A[:index + 1][::-1] + A[index+1:]
            res = [index + 1, len(A)] + self.pancakeSort(rev[1:][::-1])
        return res
