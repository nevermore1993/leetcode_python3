# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

// 简单的利用前序/中序/后序遍历来遍历二叉树就行了，将所有符合条件的结果相加
// 开始我纠结于递归调用的话没有一个全局变量来保存result，后来发现递归调用分别返回的是左右子树的总和，不需要保存结果。如果要保存的话可以利用self来
// 创建变量 self.result，这样就是类内共享的变量。
class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        result = 0
        if root == None:
            return result
        result += self.rangeSumBST(root.left,L,R)
        if root.val <= R and root.val >= L:
            result += root.val
        result += self.rangeSumBST(root.right,L,R)
        return resul
        

// 进一步优化，根据搜索二叉树的特性，左子树的值都小于根节点的值，右子树的值都大于根节点的值，所以如果根节点的值小于L，则不用再遍历其左子树
// 同理，如果根节点的值大于R，则不用遍历其右子树
// 这里还有一个函数内定义函数的用法，类似局部函数的作用？这个函数内部的函数可以使用外层函数的变量，如L,R
class Solution:
    def rangeSumBST(self, root: 'TreeNode', L: 'int', R: 'int') -> 'int':
        self.sum = 0
        
        def traverseBST(treeNode):
            if treeNode.val >= L and treeNode.val <=R:
                self.sum += treeNode.val
            if treeNode.val > L and treeNode.left:
                traverseBST(treeNode.left)
            if treeNode.val < R and treeNode.right:
                traverseBST(treeNode.right)  
            
        traverseBST(root)
        return self.sum
