// B的最大最小值肯定能够由A的最大最小值进行变换得到(因为A的其他值经过加减K得到的值肯定在A的极值经过加减K得到的范围里)
// 所以只要判断最大最小值的差距就可以了。如果在2K之内，那么说明差距可以变为0，如果大于2K，差距最小为dif-2K
class Solution:
    def smallestRangeI(self, A: List[int], K: int) -> int:
        return max(0, max(A) - min(A) - 2 * K)
