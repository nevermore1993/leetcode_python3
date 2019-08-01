// 典型的递归调用，对root的左右子树分别调用inverTree，然后再调换左右子树
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return
        right = self.invertTree(root.right)
        left = self.invertTree(root.left)
        root.left = right
        root.right = left
        return root
        
// 这种写法好像会有些问题，如果直接对root.left进行赋值，那么我们在之后对root.right进行赋值时取得就是已经变化过的root.left，也就是原来的
// root.right，那么结果会有问题。而这里在一句话中进行赋值好像并不会出现问题，是不是在一句话中就是同时进行的？
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root:
            root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root
