// 使用中序遍历，将树遍历一遍，再重新构造一棵新的树。 
// 在构造新的树的时候，我们需要在根节点前加一个dummy节点，因为我们构造树的时候，根节点的指向会一直变化，构造完成时根节点会指向
// 树的叶子，所以如果我们不保留一个根节点的copy，那么我们将失去根节点的引用。
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
