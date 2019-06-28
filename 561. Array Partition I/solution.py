// 要使所有的对中的小的元素的和最大，那么我们要尽量让小的元素大。最大的元素不可能是小的，而第二大的元素和最大的元素配对，那么他就是小的。
// 同理，第四大的元素和第三大的元素配对，第四大的就是小的。以此类推。先排序，再将所有奇数位置的数相加。
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        res = 0
        for i in range(0,len(nums),2):
            res += nums[i]
        return res

    
    
    
// 更简洁的写法   
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        #use nums[0::2] to get even
        
        nums.sort()
        return sum(nums[0::2])
