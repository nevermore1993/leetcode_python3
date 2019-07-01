// 遍历列表，两个位置指针，分别指向下一个奇数和偶数在新列表中的位置
class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        odd, even = 1, 0
        res = [0] * len(A)
        for i in A:
            if i%2 == 0:
                res[even] = i
                even += 2
            else:
                res[odd] = i
                odd += 2
        return res
