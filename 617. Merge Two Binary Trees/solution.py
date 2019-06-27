// 利用前序遍历同时遍历两棵树，遇到新的节点就创建新的节点
class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        def preOrder(t1,t2):
            if t1 and t2:
                root = TreeNode(t1.val+t2.val)
                root.left = preOrder(t1.left,t2.left)
                root.right = preOrder(t1.right,t2.right)
            elif not t1 and t2:
                root = TreeNode(t2.val)
                root.left = preOrder(None, t2.left)
                root.right = preOrder(None, t2.right)
            elif not t2 and t1:
                root = TreeNode(t1.val)
                root.left = preOrder(None, t1.left)
                root.right = preOrder(None, t1.right)
            else:
                return None
            return root
        return preOrder(t1,t2)
        
        
// 在t1的基础上创建新的树，mergeTree就是合并两棵树，可以使用递归调用
class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if t1 is None:
            return t2
        
        if t2 is None:
            return t1
        
        t1.val += t2.val
        t1.left = self.mergeTrees(t1.left, t2.left)
        t1.right = self.mergeTrees(t1.right, t2.right)
        return t1
