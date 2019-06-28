// 递归
class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        if not root.children:
            return [root.val]
        
        l = []
        for child in root.children:
            l += self.preorder(child)
        return [root.val] + l
        
        
// 循环，先遍历根节点，在将根节点的子节点入栈时，要按照相反的顺序入栈，这样我们先弹出的是靠左边的子节点。
class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not root: return []
        ans = []
        stack = [root]
        while stack:
            node = stack.pop()
            ans.append(node.val)
            for child in reversed(node.children):
                stack.append(child)
        
        return ans
