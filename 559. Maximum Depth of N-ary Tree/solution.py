// 只需要知道每个节点的深度就可以了，不需要将根节点一直保存在栈里。已经访问过的节点我们已经知道他们的深度了。
// 每次都将节点的所有儿子都入栈，然后再循环遍历。
class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if root==None:
            return 0
        stack=[(root,1)]
        depth=0
        while stack:
            node,d=stack.pop()
            depth=max(depth,d)
            for child in node.children:
                stack.append((child,d+1))
        return depth
        
// 递归      
class Solution:
    def maxDepth(self, root: 'Node') -> int:
        res = 0
        if not root:
            return 0
        if root.children:
            for root in root.children:
                res =  max(res,self.maxDepth(root))
        return 1 + res
