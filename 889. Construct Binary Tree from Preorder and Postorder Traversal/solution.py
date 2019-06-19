// 前序遍历的第一个是根节点，第二个是左子树的根节点。后序遍历的最后一个是根节点，倒数第二个是右子树的根节点。
// 或者说前序遍历中，树的根节点总是在这个树的第一个，左子树的第一个是左子树的根节点。而后序遍历中树的根节点总在最后一个，左子树的最后一个是
// 根节点
// 我们将根节点取出，在post中根据左子树根节点的值找到左右子树的遍历划分，在pre中根据右子树的根节点得到左右子树的遍历划分。然后递归调用
// 函数就可以得到结果。
class Solution:
    def constructFromPrePost(self, pre: List[int], post: List[int]) -> TreeNode:
        if len(pre) == 0:
            return None
        
        root = TreeNode(pre[0])
        if len(pre) >= 2:
            if pre[1] == post[-2]:
                root.left = self.constructFromPrePost(pre[1:], post[:-1])
            else:
                indexLeft = post.index(pre[1])
                indexRight = pre.index(post[-2])
                root.left = self.constructFromPrePost(pre[1:indexRight], post[:indexLeft+1])
                root.right = self.constructFromPrePost(pre[indexRight:],post[indexLeft+1:-1])
        return root
 

// 同样的思路，不过这里不是用根节点对应的具体索引来区分左右子树，而是根据树的长度来区分左右子树，更加简单
class Solution:
    def constructFromPrePost(self, pre: List[int], post: List[int]) -> TreeNode:
        if not pre:
            return None
        
        root = TreeNode(pre[0])
        if len(pre) == 1:
            return root

        n = post.index(pre[1]) + 1
        root.left = self.constructFromPrePost(pre[1:n + 1], post[:n])
        root.right = self.constructFromPrePost(pre[n + 1:], post[n:-1])
        return root
