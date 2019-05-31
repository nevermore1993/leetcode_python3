// 快排
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def quickSort(nums, start, end):
            if start >= end:
                return nums
            l = start
            r = end
            temp = nums[l]
            while l < r:
                while nums[r] >= temp and l < r:
                    r -= 1
                nums[l] = nums[r]
                while nums[l] < temp and l < r:
                    l += 1
                nums[r] = nums[l]
                print(l,r)
            nums[l] = temp
            quickSort(nums, start, l - 1)
            quickSort(nums, l + 1, end)
            return nums
        return quickSort(nums, 0, len(nums) - 1)
       
       
// python内置的排序，比我们自己用python实现的排序要快非常多，因为是用底层语言实现的
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        return sorted(nums)
