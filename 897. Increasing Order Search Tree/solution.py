// 使用中序遍历，将树遍历一遍，再重新构造一棵新的树
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        res = []
        def midorder(root):
            if not root:
                return None
            midorder(root.left)
            res.append(root.val)
            midorder(root.right)
        midorder(root)
        head = TreeNode(0)
        root = TreeNode(res[0])
        head.right = root
        for val in res[1:]:
            root.right = TreeNode(val)
            root = root.right
        return head.right
        
        
// 在遍历的同时就构造新的树，保存一个全局的根节点，当遍历到新的节点时，另其左儿子为None(不会影响遍历结果，因为我们已经遍历过它的左子树了)
// 另当前全局节点的右儿子指向新节点，并令新节点为全局节点。
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        
        dummy = TreeNode(0)
        self.prev = dummy
        self.inorder(root)
        return dummy.right
        
    def inorder(self, root):
        if not root:
            return

        self.inorder(root.left)
        
        root.left = None
        self.prev.right = root
        self.prev = root
        
        self.inorder(root.right)
