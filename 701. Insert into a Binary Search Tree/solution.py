# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

// 从顶至下遍历树，如果val大于当前节点，遍历其右子树，小于节点，遍历其左子树，直至找到None，将val放置于此
class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        p = root
        while p is not None:
            if p.val < val and p.right is not None:
                p = p.right
            elif p.val < val and p.right is None:
                p.right = TreeNode(val)
                break
            elif p.val > val and p.left is not None:
                p = p.left
            else:
                p.left = TreeNode(val)
                break
        
        return root
        

// 递归调用，如果大于当前节点，就变成子问题，将val插入其右子树，如果小于当前节点，就变成子问题，将val插入其左子树。如果子树为None，则将val构造
// 构造成新节点放置于此

class Solution:
    def insertIntoBST(self, root: 'TreeNode', val: 'int') -> 'TreeNode':
        if not root:
            return TreeNode(val)
        if root.val>val:
            root.left=self.insertIntoBST(root.left,val)
        else:
            root.right=self.insertIntoBST(root.right,val)
        return root
