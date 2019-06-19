// 如果要求不占用额外的空间，那么只能在原数组中记录已经出现过的值。开始我想的是将出现过的值对应的位置置为0，那么当我们检索到一个0的时候说明
// 这个位置对应的索引已经出现过一次了。但是这个方法存在一个问题，如果我们将这个位置置为0，那么这个位置本来的值就会被覆盖，我们需要在覆盖前将
// 这个位置原来的值对应的索引也置为0，就会产生一个循环，也可以处理，但是会很麻烦。所以不能简单的将一个位置置为0，需要保留原来的信息。
// 我决定给这个位置加n，因为所有的值是在1-n之间的，所以加n就一定会大于n。这样当我们遍历到一个值对应的索引是大于n的，那么说明这个值
// 已经出现过一次了
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []
        i = 0
        n = len(nums)
        for x in nums:
            if x > n:
                if nums[x - n - 1] > n:
                    res.append(x - n)
                else:
                    nums[x - n - 1] += n
            else:
                if nums[x - 1] > n:
                    res.append(x)
                else:
                    nums[x - 1] += n
        return res
        
// 还可以简单的将值取负数，也可以在记录位置的同时保留当前的信息
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []
        for x in nums:
            if nums[abs(x) - 1] < 0:
                res.append(abs(x))
            else:
                nums[abs(x) - 1] *= -1
        return res
        

// 或者使用collections.Counter()来统计所有值出现的次数，得到是字典，key是值，value是次数
// 然后返回所有value=2的key，但是这个方法使用了额外的存储空间
// 同理可以使用set
import collections

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        c = collections.Counter(nums)
        return [k for k, v in c.items() if v == 2]
