// 判断每一列的字母是否按照非降序排列，如果不是，则这一列需要去掉
class Solution:
    def minDeletionSize(self, A: List[str]) -> int:
        if len(A[0]) == 0:
            return 0
        res = 0
        for i in range(len(A[0])):
            temp = 0
            for a in A:
                if ord(a[i]) >= temp:
                    temp = ord(a[i])
                    continue
                else:
                    print(a[i])
                    res += 1
                    break
        return res
        
        
// zip() 函数用于将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的列表。
// 如果各个迭代器的元素个数不一致，则返回列表长度与最短的对象相同，利用 * 号操作符，可以将元组解压为列表。
// 这里就使用zip(*A)来将A的列取出
class Solution(object):
    def minDeletionSize(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        unsorted = 0
        for col in zip(*A):
            if list(col) != sorted(col):
                unsorted += 1
        return unsorted
