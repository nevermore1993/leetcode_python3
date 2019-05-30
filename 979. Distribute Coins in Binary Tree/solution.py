# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

// 一个叶子节点如果有a个coin，那么从这个节点出来的coin就应该有a-1个，然后这些coin到了他的父节点，父节点也就是有node.val + L + R个，那么他
// 又会有node.val + L + R - 1个coin出来。
class Solution:
    def distributeCoins(self, root: TreeNode) -> int:
        self.ans = 0

        def dfs(node):
            if not node: return 0
            L, R = dfs(node.left), dfs(node.right)
            self.ans += abs(L) + abs(R)
            return node.val + L + R - 1

        dfs(root)
        return self.ans
