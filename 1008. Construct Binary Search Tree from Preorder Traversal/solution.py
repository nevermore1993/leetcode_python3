# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


// 递归调用，函数的目的是根据前序遍历的数组构造树，而数组的第一个元素肯定是根节点。而第一个比头元素大的元素是其右子树的根节点
// 这两个元素之间的元素就是左子树的前序遍历，后面的就是右子树的前序遍历。那么只要找出右子树的根节点，然后递归调用bstFromPreorder()函数
// 来构造左右子树就可以了
class Solution(object):
    def bstFromPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: TreeNode
        """
        if len(preorder) < 1:
            return None
        
        root = TreeNode(preorder[0])
        if len(preorder) == 1:
            return root
        
        subP = preorder[1:]
        index = 0
        for i in range(len(subP)):
            index = i + 1
            if subP[i] > preorder[0]:
                index -= 1
                break
        root.left = self.bstFromPreorder(subP[:index])
        root.right = self.bstFromPreorder(subP[index:])
        return root
