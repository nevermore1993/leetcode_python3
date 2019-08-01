// 新建一个数组res，对应应该出现的所有数字，遍历nums，如果出现，就将res对应位置为1，最后遍历res查找为0的位
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        for num in nums:
            if res[num-1] == 0:
                res[num-1] = 1
        return [i+1 for i in range(len(res)) if res[i] == 0]
        
// 先将nums中的数都取出，放在set中，再遍历1-N，如果不在set中就加入结果       
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        rst = []
        setNum = set(nums)
        for i in range(1, len(nums)+1):
            if i not in setNum:
                rst.append(i)
        return rst
