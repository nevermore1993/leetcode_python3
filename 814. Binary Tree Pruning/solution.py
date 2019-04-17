# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

//既然函数的目的是返回去除了不符合条件的子树之后的树，那么我们对左右子树调用这个函数，就能够得到左右子树去除了不符合条件的子树之后的树
//有两个点要注意：1.在左右子树都修建完毕之后，不能直接返回，因为对[0,0,0]的树来说左右子树都会被剪掉，而根节点也会被剪掉，所以在修建完
//左右子树以后要重新检查一遍根节点。2.不是所有的情况都需要重新检查根节点，如果左右子树已经稳定了，即没有被修建，那么可以认为
//整个树已经稳定了，可以直接返回。而若左右子树有一个被修建了，那么就不能直接返回，要重新判断根节点
class Solution(object):
    def pruneTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root == None:
            return None
        elif root.left == None and root.right == None:
            if root.val == 0:
                return None
            else:
                return root
        else:
            l = self.pruneTree(root.left)
            r = self.pruneTree(root.right)
            if l == root.left and r == root.right:
                return root
            else:
                root.left = l
                root.right = r
                return self.pruneTree(root)
