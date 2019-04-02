# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

// 这里使用递归调用，利用list.index()得到数组中最大元素的索引，然后分别构造左右子树，因为是递归调用，所以时间复杂度较高。
// 这里还要注意一点，调用constructMaximumBinaryTree()函数时，需要通过类实例调用，self.constructMaximumBinaryTree()
// 或者Solution.constructMaximumBinaryTree(self,nums)来调用，因为这个函数的参数里有self，也就是与类实例绑定的，那么我们
// 在调用的时候需要指定类实例。
// 而对于没有self参数的函数，我们调用的时候只需要通过类名就可以调用，不需要也不能够给其指定类实例。

class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        if len(nums) < 1:
            return None
        
        maxIndex = nums.index(max(nums))
        root = TreeNode(nums[maxIndex])
        root.left = self.constructMaximumBinaryTree(nums[:maxIndex])
        root.right = self.constructMaximumBinaryTree(nums[maxIndex+1:])
        return root
        
        
// 遍历数组构造，如果当前元素比前一个元素小，则当前元素为前一个元素的右儿子，如果当前元素比前一个元素大，前一元素为当前元素的
// 左儿子，并重复当前操作，向前遍历，直到stack中没有元素了。 stack中第一个元素一定是当前已经遍历过的数组中最大的元素，之后的元素
// 是当前最大元素右子树中的元素的降序排列。每次循环末尾，当前元素都需要添加到stack中，因为下一个元素需要与当前元素比较。
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        stack = []
        for index in range(0,len(nums)):
            current = TreeNode(nums[index])
            while stack and stack[-1].val < nums[index]:
                current.left = stack.pop()
            if stack:
                stack[-1].right = current
            stack.append(current)
        return stack[0]
