// 递归调用，先访问所有的子节点，再访问自己。这里postorder返回的是当前根节点的遍历。所以循环中是所有兄弟子节点的遍历的联合
class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if not root: 
            return []
        if not root.children: 
            return [root.val]
        l = []
        for c in root.children: 
            l += self.postorder(c)
        return l + [root.val]
        
        
        
        
// 循环方法。首先将根节点和所有最左子树入栈。当节点的所有儿子都遍历过了之后，弹出该节点。
// 如果最后一个节点有其他的子节点，再按序将这些节点入栈。重复步骤。
class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        ans = []
        st = []
        if not root:
            return []
        while root or st:
            while root:
                st.append((root,0))
                root = root.children[0] if root.children else None
            node, i = st.pop()
            ans.append(node.val)
            while st and len(st[-1][0].children) == i + 1:
                node, i = st.pop()
                ans.append(node.val)
            if not st:
                break
            node = st[-1][0].children[i+1]
            st.append((node ,i+1))
            root = node.children[0] if node.children else None
            # print(ans)
        return ans
