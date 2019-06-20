// 要找的的是最大的差距，所以在每个节点，需要找到这个节点的左右子树中的最大与最小值，并计算最大的差距，然后更新res。
// dfs函数的目的是找出当前节点左右子树的最大最小值。
class Solution:
    def maxAncestorDiff(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = 0
        self.dfs(root, None)
        return self.res
        
    def dfs(self, node, parent):
        if node:
            min_l, max_l = self.dfs(node.left, node)
            min_r, max_r = self.dfs(node.right, node)
            self.res = max(abs(node.val - min_l), abs(node.val - min_r), abs(node.val - max_r), abs(node.val - max_l), self.res)
            return min(min_l, min_r, node.val), max(max_r, max_l, node.val)
        return parent.val, parent.val
