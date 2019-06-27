// 开始我想用判断数组中超过半数的元素的方法，就是遍历数组，不同的元素抵消，相同的元素加数量，最后剩下的元素就是超过半数的元素
// 但是这里不行，因为是对半分的，所以可能会出现什么都不剩的情况。
class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        s = set()
        for i in A:
            if i in s:
                return i
            else:
                s.add(i)
