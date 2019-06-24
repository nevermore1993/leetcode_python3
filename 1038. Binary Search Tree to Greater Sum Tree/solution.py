// 前序遍历，得到的就是按照大小排序的节点，然后从后往前遍历，节点数值累加
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        nodes = []
        def preorder(root):
            if not root:
                return
            preorder(root.left)
            nodes.append(root)
            preorder(root.right)
        
        preorder(root)
        if len(nodes) <= 1:
            return root
        else:
            for i in range(len(nodes)-2,-1,-1):
                nodes[i].val += nodes[i+1].val
            return root
            
            
// 以 右子树-根-左子树的顺序开始遍历，即从最大的节点开始。在遍历的同时将每个节点的值叠加起来。因为新的节点的值就是它本身的值和比他大的值
// 的累加。这样在一次遍历中就可以完成更新
class Solution:
    
    # replace each node's value with the sum of it's right child tree
    
    # right child - 
    
    # iterate from greatest to smallest, adding the value to collective sum at each step
    
    # right child, then itself, then left child
    
    running_sum = None
    def bstToGst(self, root: TreeNode) -> TreeNode:
        self.running_sum = 0
        self.bstToGstHelper(root)
        return root
    
    def bstToGstHelper(self, curr: TreeNode) -> None:
        if curr.right:
            self.bstToGstHelper(curr.right)
        self.running_sum += curr.val
        curr.val = self.running_sum
        if curr.left:
            self.bstToGstHelper(curr.left)
