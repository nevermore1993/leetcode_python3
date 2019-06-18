// 分两个函数，第一个函数将树结构转换为数组，第二个函数将数组转换为树结构，都利用递归的方法
class Solution:
    def insertIntoMaxTree(self, root: TreeNode, val: int) -> TreeNode:
        
        def root2array(root):
            res = []
            if root is None:
                return res
            
            res.append(root.val)
            
            return root2array(root.left) + res + root2array(root.right)
        
        def array2tree(array: list):
            if array is None:
                return None
            if len(array) == 0:
                return None
            maxIndex = array.index(max(array))
            root = TreeNode(array[maxIndex])
            root.left = array2tree(array[:maxIndex])
            root.right = array2tree(array[maxIndex+1:])
            return root
                 
        array = root2array(root)
        array.append(val)
        return array2tree(array)
        

// 如果新添加的元素比根节点要大，那么它将成为新的树的根节点，原树整体成为新根节点的左子树(因为新的元素是添加在数组末尾的)
// 如果新添加的元素没有根节点大，那么他也只会改变原根节点的右子树，因为他在末尾，所以肯定在原根节点的右边，那么递归调用函数，重构右子树
// 就可以了。
class Solution:
    def insertIntoMaxTree(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return TreeNode(val)
        if root.val < val:
            newroot = TreeNode(val)
            newroot.left = root
            return newroot
        root.right = self.insertIntoMaxTree(root.right, val)
        return root
