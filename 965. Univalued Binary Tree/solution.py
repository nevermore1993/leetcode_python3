// 如果根节点和左右儿子的值一样，且左右子树都是univalued，那么说明这棵树是univalued，可以使用递归的方法判断
// 也可以遍历整颗树来判断是不是univalued，我认为效率应该是差不多的，都需要对树进行一次遍历
class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        if not root:
            return True
        val = root.val
        left = root.left
        right = root.right
        if left and right:
            if val == left.val == right.val and self.isUnivalTree(left) and self.isUnivalTree(right):
                return True
            else:
                return False
        elif not left and right:
            if val == right.val and self.isUnivalTree(right):
                return True
            else:
                return False
        elif left and not right:
            if val == left.val and self.isUnivalTree(left):
                return True
            else:
                return False
        else:
            return True
            
            
// 同样的递归调用，不过更简洁      
class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        if not root:
            return True
        if root.left and root.left.val != root.val:
            return False
        if root.right and root.right.val != root.val:
            return False
        return self.isUnivalTree(root.left) and self.isUnivalTree(root.right)
          
class Solution:
    def isUnivalTree(self, root):
        left_correct = (not root.left or root.val == root.left.val
                and self.isUnivalTree(root.left))
        right_correct = (not root.right or root.val == root.right.val
                and self.isUnivalTree(root.right))
        return left_correct and right_correct
